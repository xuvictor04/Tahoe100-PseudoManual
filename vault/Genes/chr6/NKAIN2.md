---
symbol: "NKAIN2"
type: "gene"
col: 12026
ensembl_id: "ENSG00000188580"
name: "sodium/potassium transporting ATPase interacting 2"
location: "6q22.31"
module: 19
arm: "+"
pooled_cpm: 17.06
n_lines_expressing: 18
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 19
direction_downstream: 17
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# NKAIN2

*sodium/potassium transporting ATPase interacting 2* — 6q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.91× (z +23.6, q 0e+00, up in 10 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.621× (z -4.5, q 0.005, down in 9 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.249×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.242×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCDH15]] (+0.77, fdr 7e-06), [[MARCHF1]] (+0.75, fdr 7e-06), [[IQCM]] (+0.71, fdr 1e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 17 go from it, the strongest it → [[LSAMP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12026.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.91×** | +23.6 | 0e+00 | 10/13 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.09×** | +15.0 | 0e+00 | 8/15 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.63×** | +14.4 | 1e-44 | 8/10 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.71×** | +12.3 | 1e-32 | 11/15 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.64×** | +11.7 | 2e-29 | 2/5 (PANC-1, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.20×** | +10.5 | 1e-23 | 10/16 (PANC-1, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.61×** | +8.3 | 7e-15 | 4/7 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +5.9 | 2e-07 | 3/13 (LOX-IMVI, HT-29, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.80×** | +5.5 | 2e-06 | 7/15 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.78×** | +5.4 | 4e-06 | 5/13 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +5.3 | 6e-06 | 3/11 (SNU-423, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.2 | 1e-05 | 4/16 (SW 900, SK-MEL-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +4.1 | 0.002 | 8/14 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +4.1 | 0.002 | 3/12 (NCI-H23, PANC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +4.0 | 0.002 | 7/14 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.54×** | +3.9 | 0.003 | 7/13 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +3.6 | 0.010 | 5/14 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.063 | 2/13 (CFPAC-1, HCT15) | inconsistent across doses |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.37×** | +3.0 | 0.084 | 2/15 (NCI-H460, PANC-1) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12026.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.249×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.242×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.621×** | -4.5 | 0.005 | 9/15 (LOX-IMVI, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.704× | -3.3 | 0.22 | 2/15 (SHP-77, NCI-H23) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.688× | -3.2 | 0.22 | 1/15 (AN3 CA) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12026. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 14.1 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 26.3× (z +15.9) | — |
| [[A-172 (line)]] | wt | 7.02 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 90.5× (z +23.3) | — |
| [[LOX-IMVI (line)]] | wt | 4.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.6× (z +11.3) | — |
| [[NCI-H23 (line)]] | alt | 9.32 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 16.3× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 38.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -8.5) |
| [[SHP-77 (line)]] | alt | 620 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -13.9) |
| [[SNU-423 (line)]] | alt | 7.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 73.5× (z +19.4) | — |
| [[A-427 (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.96 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.15 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.86 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.07 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.88 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.96 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.58 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.95 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12026), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCDH15]] | +0.77 | +0.70 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[MARCHF1]] | +0.75 | +0.70 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[IQCM]] | +0.71 | +0.54 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[KCNMB2]] | +0.71 | +0.57 / +0.72 | both halves | 1e-05 | **novel candidate** |
| [[ASXL3]] | +0.70 | +0.57 / +0.74 | both halves | 9e-06 | **novel candidate** |
| [[CRISPLD1]] | +0.69 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[KCNJ6]] | +0.68 | +0.59 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[LSAMP]] | +0.68 | +0.56 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[KCNH7]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[PCDH9]] | +0.67 | +0.65 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[RAB3C]] | +0.66 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[LINC01035]] | +0.65 | +0.59 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 1, C 18. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NKAIN2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01508]] | C | LINC01508 activity raises NKAIN2's level | lines that do not express LINC01508 (42) vs lines expressing it (8) | 3.54× lower at baseline in the lines without LINC01508 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, SPINK13, RHEX; co-absent with the target |
| [[ADARB2]] | C | ADARB2 activity raises NKAIN2's level | lines that do not express ADARB2 (39) vs lines expressing it (11) | 3.25× lower at baseline in the lines without ADARB2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, GSG1L2; co-absent with the target |
| [[DPP10]] | C | DPP10 activity raises NKAIN2's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 3.21× lower at baseline in the lines without DPP10 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises NKAIN2's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 4.77× lower at baseline in the lines without SYT4 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[LINC01035]] | C | LINC01035 activity raises NKAIN2's level | lines that do not express LINC01035 (43) vs lines expressing it (7) | 5.44× lower at baseline in the lines without LINC01035 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, CALCA, GSG1L2; co-absent with the target |
| [[POU6F2]] | C | POU6F2 activity raises NKAIN2's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 2.29× lower at baseline in the lines without POU6F2 | 0.024 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent; co-absent with the target |
| [[PCSK1]] | C | PCSK1 activity raises NKAIN2's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 2.93× lower at baseline in the lines without PCSK1 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2; co-absent with the target |
| [[ASCL1]] | C | ASCL1 activity raises NKAIN2's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 2.86× lower at baseline in the lines without ASCL1 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[KCNB2]] | C | KCNB2 activity raises NKAIN2's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 3.45× lower at baseline in the lines without KCNB2 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises NKAIN2's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 4.34× lower at baseline in the lines without RIT2 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[TENM1]] | C | TENM1 activity raises NKAIN2's level | lines that do not express TENM1 (29) vs lines expressing it (21) | 1.97× lower at baseline in the lines without TENM1 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, MIR4307HG; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 4, C 13. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LSAMP]] | B | NKAIN2 activity raises LSAMP's level | lines that do not express NKAIN2 (32) vs lines expressing it (18) | 3.29× lower at baseline in the lines without NKAIN2 | 0.017 | ⚠ within organs, on part of the lines; also absent: GREM2, ASCL1, ENSG00000289309; maybe low, not absent |
| [[LSAMP]] | B | NKAIN2 activity weakens LSAMP's drug response | lines that do not express NKAIN2 (19) vs lines expressing it (12) | (z diff -3.94); strongest at Idarubicin (hydrochloride) 5 µM: 1.51x vs 0.47x (z diff -8.6) | 0.039 | ⚠ within organs, on part of the lines; also absent: GREM2, ASCL1, ENSG00000289309; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PCDH15]] | B | NKAIN2 activity raises PCDH15's level | lines that do not express NKAIN2 (32) vs lines expressing it (18) | 2.23× lower at baseline in the lines without NKAIN2 | 0.048 | ⚠ within organs, on part of the lines; also absent: GREM2, ASCL1, ENSG00000289309; maybe low, not absent |
| [[LINC02306]] | B | NKAIN2 activity raises LINC02306's level | lines that do not express NKAIN2 (32) vs lines expressing it (18) | 1.73× lower at baseline in the lines without NKAIN2 | 0.050 | ⚠ within organs, on part of the lines; also absent: GREM2, ASCL1, ENSG00000289309; maybe low, not absent |
| [[ADARB2]] | C | NKAIN2 activity raises ADARB2's level | lines that do not express NKAIN2 (32) vs lines expressing it (18) | 2.84× lower at baseline in the lines without NKAIN2 | 0.019 | ⚠ within organs, on part of the lines; also absent: GREM2, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[MARCHF1]] | C | NKAIN2 activity raises MARCHF1's level | lines that do not express NKAIN2 (32) vs lines expressing it (18) | 3.30× lower at baseline in the lines without NKAIN2 | 0.033 | ⚠ within organs, on part of the lines; also absent: GREM2, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[LINC01035]] | C | NKAIN2 activity raises LINC01035's level | lines that do not express NKAIN2 (32) vs lines expressing it (18) | 2.41× lower at baseline in the lines without NKAIN2 | 0.039 | ⚠ within organs, on part of the lines; also absent: GREM2, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[FGF14]] | C | NKAIN2 activity raises FGF14's level | lines that do not express NKAIN2 (32) vs lines expressing it (18) | 2.59× lower at baseline in the lines without NKAIN2 | 0.048 | ⚠ within organs, on part of the lines; also absent: GREM2, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[VIPR2]] | C | NKAIN2 activity raises VIPR2's level | lines that do not express NKAIN2 (32) vs lines expressing it (18) | 1.40× lower at baseline in the lines without NKAIN2 | 0.054 | ⚠ within organs, on part of the lines; also absent: GREM2, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[TENM1]] | C | NKAIN2 activity raises TENM1's level | lines that do not express NKAIN2 (32) vs lines expressing it (18) | 2.59× lower at baseline in the lines without NKAIN2 | 0.054 | ⚠ within organs, on part of the lines; also absent: GREM2, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[QPCT]] | C | NKAIN2 activity raises QPCT's level | lines that do not express NKAIN2 (32) vs lines expressing it (18) | 1.99× lower at baseline in the lines without NKAIN2 | 0.056 | ⚠ within organs, on part of the lines; also absent: GREM2, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[LINC03000]] | C | NKAIN2 activity raises LINC03000's level | lines that do not express NKAIN2 (32) vs lines expressing it (18) | 2.36× lower at baseline in the lines without NKAIN2 | 0.068 | ⚠ within organs, on part of the lines; also absent: GREM2, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.0, 34.4); signed map (42.3, 38.4). **Vector** length 38.7, 10.2% of its response variance represented; |z| ≥ 3 in 309 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.1 | +14.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +23.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +3.9 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.5 | -4.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -3.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.4 | -2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | sodium/potassium transporting ATPase interacting 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.31 — chr6:123,803,865-124,825,640 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FAM77B; previously TCBA1 |
| Gene groups (HGNC) | Na+/K+ transporting ATPase interacting |
| Matched by | ensembl_id |

UniProt [Q5VXU1](https://www.uniprot.org/uniprotkb/Q5VXU1) carries no function annotation.

**Summary**, from NCBI Gene [154215](https://www.ncbi.nlm.nih.gov/gene/154215):

> This gene encodes a transmembrane protein that interacts with the beta subunit of a sodium/potassium-transporting ATPase. A chromosomal translocation involving this gene is a cause of lymphoma. Alternative splicing results in multiple transcript variants encoding distinct isoforms. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:16443](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16443) · Entrez [154215](https://www.ncbi.nlm.nih.gov/gene/154215) · UniProt [Q5VXU1](https://www.uniprot.org/uniprotkb/Q5VXU1) · Ensembl [ENSG00000188580](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188580)

## Data

Gene col 12026: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12026); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12026, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12026]; `tensor/DDL_lfc|DDL_z.npy` [12026]; `embed/gene_vectors.npy` [12026]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12026 or target_col == 12026). Every well: [[NKAIN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NKAIN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
