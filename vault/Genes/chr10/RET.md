---
symbol: "RET"
type: "gene"
col: 9177
ensembl_id: "ENSG00000165731"
name: "ret proto-oncogene"
location: "10q11.21"
module: 82
arm: "+"
pooled_cpm: 2.57
n_lines_expressing: 22
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 43
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# RET

*ret proto-oncogene* — 10q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.78× (z +11.9, q 6e-30, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.62× (z +10.8, q 1e-24, up in 10 of 14 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 0.114×, LoVo 0.163×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.208×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (LoVo 0.0719×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JAKMIP1]] (+0.75, fdr 7e-06), [[ADCY1]] (+0.70, fdr 7e-06), [[KCNK13]] (+0.67, fdr 7e-06).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[OCA2]] → it (grade B ⚠); 43 go from it, the strongest it → [[EBF4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9177.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.78×** | +11.9 | 6e-30 | 1/3 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.62×** | +10.8 | 1e-24 | 10/14 (A549, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.52×** | +9.9 | 5e-21 | 5/7 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.35×** | +9.5 | 2e-19 | 13/17 (A-427, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.16×** | +8.4 | 4e-15 | 1/4 (SHP-77) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.90×** | +8.4 | 4e-15 | 11/17 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.55×** | +7.4 | 1e-11 | 12/17 (PANC-1, NCI-H2030, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.25×** | +6.4 | 1e-08 | 13/17 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +5.8 | 4e-07 | 7/12 (A549, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.14×** | +5.7 | 5e-07 | 2/8 (A-172, LoVo) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.05×** | +5.6 | 8e-07 | 10/17 (PANC-1, SW 900, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.63×** | +5.4 | 2e-06 | 1/7 (LoVo) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.92×** | +5.1 | 1e-05 | 7/17 (MIA PaCa-2, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.76×** | +4.4 | 3e-04 | 9/13 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.72×** | +4.2 | 8e-04 | 0/11 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.95×** | +3.7 | 0.006 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +3.6 | 0.010 | 3/16 (A-172, HOP62, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.79×** | +3.3 | 0.032 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.48×** | +2.9 | 0.095 | 1/14 (SHP-77) | inconsistent across doses |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.47×** | +2.9 | 0.095 | 0/13 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9177.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 0.114×, LoVo 0.163×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.208×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (LoVo 0.0719×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | 0.682× | -3.1 | 0.43 | 9/16 (MIA PaCa-2, A549, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.764× | -3.1 | 0.43 | 3/17 (CHP-212, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9177. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 1.73 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 26.5× (z +10.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 19.7× (z +9.6) | — |
| [[LoVo (line)]] | wt | 3.53 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -9.8) |
| [[A-172 (line)]] | wt | 3.86 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -10.5) |
| [[A549 (line)]] | wt | 2.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +9.9) | — |
| [[CHP-212 (line)]] | wt | 149 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -9.4) |
| [[A-427 (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.268 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.324 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.288 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.291 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.294 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.307 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.282 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.316 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.340 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.430 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.867 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.245 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.243 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.561 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.635 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.645 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.382 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.304 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9177), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JAKMIP1]] | +0.75 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[ADCY1]] | +0.70 | +0.64 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[KCNK13]] | +0.67 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[CHST8]] | +0.66 | +0.58 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[DPYSL5]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[KCNQ2]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[NOVA2]] | +0.64 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[GPC3]] | +0.64 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[UBE2QL1]] | +0.62 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[LMX1B]] | +0.61 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[SLC6A17]] | +0.60 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[CACNA2D2]] | +0.60 | +0.54 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 2, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OCA2]] | B | OCA2 activity raises RET's level | lines that do not express OCA2 (18) vs lines expressing it (32) | 1.06× lower at baseline in the lines without OCA2 | 0.025 | ⚠ within organs, on part of the lines; also absent: BEX4, STAC, ATP10A; maybe low, not absent |
| [[SEPTIN3]] | B | SEPTIN3 activity raises RET's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 2.29× lower at baseline in the lines without SEPTIN3 | 0.074 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[NFASC]] | C | NFASC activity raises RET's level | lines that do not express NFASC (27) vs lines expressing it (23) | 2.49× lower at baseline in the lines without NFASC | 0.030 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A; co-absent with the target |
| [[C14orf132]] | C | C14orf132 activity raises RET's level | lines that do not express C14orf132 (19) vs lines expressing it (31) | 2.22× lower at baseline in the lines without C14orf132 | 0.032 | ⚠ within organs, on part of the lines; also absent: SLC22A17, ZFP28, ADAMTS7; co-absent with the target |
| [[MED12L]] | C | MED12L activity raises RET's level | lines that do not express MED12L (18) vs lines expressing it (32) | 2.58× lower at baseline in the lines without MED12L | 0.033 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2; co-absent with the target |
| [[DPYSL5]] | C | DPYSL5 activity raises RET's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 2.04× lower at baseline in the lines without DPYSL5 | 0.036 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5; co-absent with the target |
| [[KIF26A]] | C | KIF26A activity raises RET's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.43× lower at baseline in the lines without KIF26A | 0.039 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN; co-absent with the target |
| [[LRRN2]] | C | LRRN2 activity raises RET's level | lines that do not express LRRN2 (30) vs lines expressing it (20) | 2.71× lower at baseline in the lines without LRRN2 | 0.042 | ⚠ within organs, on part of the lines; also absent: LGSN, KIF1A, NEFL; co-absent with the target |
| [[LHX2]] | C | LHX2 activity raises RET's level | lines that do not express LHX2 (26) vs lines expressing it (24) | 1.79× lower at baseline in the lines without LHX2 | 0.049 | ⚠ within organs, on part of the lines; also absent: CECR2, COL4A4, GHR; co-absent with the target |
| [[PHF21B]] | C | PHF21B activity raises RET's level | lines that do not express PHF21B (21) vs lines expressing it (29) | 2.49× lower at baseline in the lines without PHF21B | 0.059 | ⚠ within organs, on part of the lines; also absent: JAM3, ADAM23, ADD2; co-absent with the target |
| [[SNAP91]] | C | SNAP91 activity raises RET's level | lines that do not express SNAP91 (26) vs lines expressing it (24) | 2.46× lower at baseline in the lines without SNAP91 | 0.091 | ⚠ within organs, on part of the lines; also absent: CHST8, PLEKHG4B, COLEC12; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 23, C 20. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EBF4]] | B | RET activity raises EBF4's level | lines that do not express RET (28) vs lines expressing it (22) | 2.75× lower at baseline in the lines without RET | 8e-04 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[MAN1C1]] | B | RET activity raises MAN1C1's level | lines that do not express RET (28) vs lines expressing it (22) | 2.03× lower at baseline in the lines without RET | 0.011 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[SEPTIN3]] | B | RET activity raises SEPTIN3's level | lines that do not express RET (28) vs lines expressing it (22) | 2.31× lower at baseline in the lines without RET | 0.012 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[GPRIN1]] | B | RET activity raises GPRIN1's level | lines that do not express RET (28) vs lines expressing it (22) | 1.84× lower at baseline in the lines without RET | 0.014 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[NKAIN1]] | B | RET activity raises NKAIN1's level | lines that do not express RET (28) vs lines expressing it (22) | 1.87× lower at baseline in the lines without RET | 0.018 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[RASGEF1C]] | B | RET activity raises RASGEF1C's level | lines that do not express RET (28) vs lines expressing it (22) | 1.94× lower at baseline in the lines without RET | 0.019 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[PARD6G]] | B | RET activity raises PARD6G's level | lines that do not express RET (28) vs lines expressing it (22) | 2.16× lower at baseline in the lines without RET | 0.031 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[CAMK2B]] | B | RET activity raises CAMK2B's level | lines that do not express RET (28) vs lines expressing it (22) | 1.87× lower at baseline in the lines without RET | 0.036 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[TSPAN33]] | B | RET activity raises TSPAN33's level | lines that do not express RET (28) vs lines expressing it (22) | 1.64× lower at baseline in the lines without RET | 0.044 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[KCNK13]] | B | RET activity raises KCNK13's level | lines that do not express RET (28) vs lines expressing it (22) | 1.51× lower at baseline in the lines without RET | 0.046 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[CDH23]] | B | RET activity raises CDH23's level | lines that do not express RET (28) vs lines expressing it (22) | 1.89× lower at baseline in the lines without RET | 0.052 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[TMEM150C]] | B | RET activity raises TMEM150C's level | lines that do not express RET (28) vs lines expressing it (22) | 2.58× lower at baseline in the lines without RET | 0.052 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.734). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.7, 38.8); signed map (27.3, 27.5). **Vector** length 33.9, 6.28% of its response variance represented; |z| ≥ 3 in 507 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +9.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +10.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +2.2 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -2.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.2 | -3.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -2.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ret proto-oncogene |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.21 — chr10:43,077,064-43,130,351 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PTC, CDHF12, RET51, CDHR16; previously HSCR1, MEN2A, MTC1, MEN2B |
| Gene groups (HGNC) | Cadherin related; Ret proto-oncogene family |
| Hallmark sets | UV_RESPONSE_UP, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 11 pathways, smallest: Formation of the nephric duct; Formation of the ureteric bud; NPAS4 regulates expression of target genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P07949](https://www.uniprot.org/uniprotkb/P07949) (Proto-oncogene tyrosine-protein kinase receptor Ret):

> Receptor tyrosine-protein kinase involved in numerous cellular mechanisms including cell proliferation, neuronal navigation, cell migration, and cell differentiation in response to glia cell line-derived growth family factors (GDNF, NRTN, ARTN, PSPN and GDF15). In contrast to most receptor tyrosine kinases, RET requires not only its cognate ligands but also coreceptors, for activation. GDNF ligands (GDNF, NRTN, ARTN, PSPN and GDF15) first bind their corresponding GDNFR coreceptors (GFRA1, …

**Summary**, from NCBI Gene [5979](https://www.ncbi.nlm.nih.gov/gene/5979):

> This gene encodes a transmembrane receptor and member of the tyrosine protein kinase family of proteins. Binding of ligands such as GDNF (glial cell-line derived neurotrophic factor) and other related proteins to the encoded receptor stimulates receptor dimerization and activation of downstream signaling pathways that play a role in cell differentiation, growth, migration and survival. The encoded receptor is important in development of the nervous system, and the development of organs and …

**Accessions** — [HGNC:9967](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9967) · Entrez [5979](https://www.ncbi.nlm.nih.gov/gene/5979) · UniProt [P07949](https://www.uniprot.org/uniprotkb/P07949) · Ensembl [ENSG00000165731](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165731)

## Data

Gene col 9177: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9177); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9177, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9177]; `tensor/DDL_lfc|DDL_z.npy` [9177]; `embed/gene_vectors.npy` [9177]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9177 or target_col == 9177). Every well: [[RET — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RET.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
