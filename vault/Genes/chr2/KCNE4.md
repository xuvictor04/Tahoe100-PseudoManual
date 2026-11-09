---
symbol: "KCNE4"
type: "gene"
col: 7585
ensembl_id: "ENSG00000152049"
name: "potassium voltage-gated channel subfamily E regulatory subunit 4"
location: "2q36.1"
module: 19
arm: "+"
pooled_cpm: 12.94
n_lines_expressing: 16
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 46
direction_downstream: 56
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# KCNE4

*potassium voltage-gated channel subfamily E regulatory subunit 4* — 2q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.59× (z +16.5, q 0e+00, up in 2 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.81× (z +8.0, q 1e-13, up in 1 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.572× (z -5.4, q 5e-05, down in 11 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDE3A]] (+0.77, fdr 7e-06), [[PDGFRB]] (+0.70, fdr 7e-06), [[SLCO1C1]] (+0.69, fdr 7e-06); moves opposite to [[KIF13B]] (-0.46, fdr 3e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 46 arrows point to it, the strongest [[RNF152]] → it (grade B ⚠); 56 go from it, the strongest it → [[TENT5A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7585.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.59×** | +16.5 | 0e+00 | 2/12 (CFPAC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.41×** | +15.6 | 0e+00 | 1/10 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.36×** | +10.7 | 1e-24 | 2/10 (CFPAC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +8.0 | 1e-13 | 1/12 (A498) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.11×** | +7.1 | 1e-10 | 6/14 (A-172, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +6.2 | 4e-08 | 2/11 (CFPAC-1, C32) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +4.8 | 1e-04 | 0/13 | top dose only | cell-cycle shift (explains ~8% here) |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.9 | 0.007 | 2/14 (HS-578T, CFPAC-1) | top dose only | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.34×** | +3.9 | 0.007 | 1/7 (SHP-77) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.096 | 0/14 | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.096 | 2/14 (CFPAC-1, A498) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7585.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.572×** | -5.4 | 5e-05 | 11/14 (hTERT-HPNE, SHP-77, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.622×** | -4.6 | 0.001 | 8/13 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.636×** | -4.3 | 0.003 | 3/14 (SNU-423, SW 1088, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.647×** | -4.0 | 0.008 | 9/13 (AN3 CA, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.671×** | -3.8 | 0.015 | 6/14 (A-172, SW 1088, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.704×** | -3.4 | 0.073 | 5/13 (NCI-H460, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.707× | -3.2 | 0.11 | 9/12 (hTERT-HPNE, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.711× | -3.0 | 0.17 | 0/14 | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | 0.731× | -3.0 | 0.17 | 2/14 (SNU-423, hTERT-HPNE) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7585. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 214 | 0 | 13 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0209× (z -23.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0419× (z -19.0) |
| [[SHP-77 (line)]] | alt | 171 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.125× (z -20.0) |
| [[NCI-H460 (line)]] | wt | 64.3 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.134× (z -10.9) |
| [[AN3 CA (line)]] | alt | 121 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -12.9) |
| [[RPMI-7951 (line)]] | alt | 49.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0592× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.168× (z -8.5) |
| [[HS-578T (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.129× (z -9.2) ⚠ cell-cycle shift, explains ~18% of this change |
| [[SW 1088 (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0308× (z -9.1) ⚠ cell-cycle shift, explains ~18% of this change |
| [[A-172 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.69 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7585), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE3A]] | +0.77 | +0.76 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[PDGFRB]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[SLCO1C1]] | +0.69 | +0.68 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[CDH7]] | +0.67 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[DOK6]] | +0.64 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[BAALC]] | +0.63 | +0.55 / +0.72 | both halves | 1e-05 | **novel candidate** |
| [[GREM2]] | +0.63 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[CARMN]] | +0.62 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[ADGRB3]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[ARHGEF6]] | +0.61 | +0.60 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[TCF4]] | +0.60 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[SDC2]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF13B]] | -0.46 | -0.43 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 3, C 43. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF152]] | B | RNF152 activity raises KCNE4's level | lines that do not express RNF152 (18) vs lines expressing it (32) | 3.06× lower at baseline in the lines without RNF152 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, SNCAIP, OR9Q1; maybe low, not absent |
| [[APLN]] | B | APLN activity raises KCNE4's level | lines that do not express APLN (13) vs lines expressing it (37) | 2.39× lower at baseline in the lines without APLN | 0.083 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[KCNMB2]] | B | KCNMB2 activity raises KCNE4's level | lines that do not express KCNMB2 (18) vs lines expressing it (32) | 2.04× lower at baseline in the lines without KCNMB2 | 0.091 | ⚠ within organs, on part of the lines; also absent: LINC01980, LINC02398, LINC02306; maybe low, not absent |
| [[PDZRN3]] | C | PDZRN3 activity raises KCNE4's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 3.94× lower at baseline in the lines without PDZRN3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098; co-absent with the target |
| [[LOXL3]] | C | LOXL3 activity raises KCNE4's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 3.88× lower at baseline in the lines without LOXL3 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises KCNE4's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 6.28× lower at baseline in the lines without PDGFRB | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[HGF]] | C | HGF activity raises KCNE4's level | lines that do not express HGF (38) vs lines expressing it (12) | 5.44× lower at baseline in the lines without HGF | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA; co-absent with the target |
| [[EDNRB]] | C | EDNRB activity raises KCNE4's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 4.92× lower at baseline in the lines without EDNRB | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[COL3A1]] | C | COL3A1 activity raises KCNE4's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 4.66× lower at baseline in the lines without COL3A1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677; co-absent with the target |
| [[SCARA5]] | C | SCARA5 activity raises KCNE4's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 8.52× lower at baseline in the lines without SCARA5 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[TRPA1]] | C | TRPA1 activity raises KCNE4's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 4.08× lower at baseline in the lines without TRPA1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; co-absent with the target |
| [[GREM2]] | C | GREM2 activity raises KCNE4's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 7.29× lower at baseline in the lines without GREM2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054; co-absent with the target |

### Downstream of this gene

*56 arrows, 56 of them with an alert ⚠; grade A 0, B 13, C 43. Shown: the 12 strongest; 44 more arrows (44 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TENT5A]] | B | KCNE4 activity raises TENT5A's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 3.82× lower at baseline in the lines without KCNE4 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN |
| [[SLCO1C1]] | B | KCNE4 activity raises SLCO1C1's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 2.02× lower at baseline in the lines without KCNE4 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN |
| [[KCNMB2]] | B | KCNE4 activity raises KCNMB2's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 2.42× lower at baseline in the lines without KCNE4 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN |
| [[SLC14A2]] | B | KCNE4 activity raises SLC14A2's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 2.58× lower at baseline in the lines without KCNE4 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN |
| [[RNF152]] | B | KCNE4 activity raises RNF152's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 3.32× lower at baseline in the lines without KCNE4 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN |
| [[TNFRSF19]] | B | KCNE4 activity raises TNFRSF19's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 2.51× lower at baseline in the lines without KCNE4 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN |
| [[SEMA6D]] | B | KCNE4 activity raises SEMA6D's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 2.48× lower at baseline in the lines without KCNE4 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN |
| [[PCBP3]] | B | KCNE4 activity raises PCBP3's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 3.10× lower at baseline in the lines without KCNE4 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN |
| [[CFAP20DC-DT]] | B | KCNE4 activity raises CFAP20DC-DT's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 1.75× lower at baseline in the lines without KCNE4 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN |
| [[TMEM45A]] | B | KCNE4 activity strengthens TMEM45A's drug response | lines that do not express KCNE4 (22) vs lines expressing it (13) | the lines without KCNE4 respond 0.73× as strongly (z diff +2.54); strongest at Harringtonine 5 µM: 0.36x vs 0.17x (z diff +4.2) | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN; target measured in part of the lines; artifact flags |
| [[TMEM45A]] | B | KCNE4 activity raises TMEM45A's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 3.84× lower at baseline in the lines without KCNE4 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN |
| [[ANO3]] | B | KCNE4 activity raises ANO3's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 1.96× lower at baseline in the lines without KCNE4 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.552). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.7, 21.2); signed map (36.5, 43.9). **Vector** length 61.2, 23.8% of its response variance represented; |z| ≥ 3 in 364 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.1 | +16.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +15.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +10.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | -0.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +3.1 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -2.0 | -3.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.9 | -1.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -2.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel subfamily E regulatory subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.1 — chr2:223,052,190-223,198,399 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MiRP3 |
| Gene groups (HGNC) | Potassium voltage-gated channel regulatory subunits |
| Reactome | 4 pathways, smallest: Phase 3 - rapid repolarisation; Phase 2 - plateau phase; Cardiac conduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWG9](https://www.uniprot.org/uniprotkb/Q8WWG9) (Potassium voltage-gated channel subfamily E member 4):

> Ancillary protein that functions as a regulatory subunit of the voltage-gated potassium (Kv) channel complex composed of pore-forming and potassium-conducting alpha subunits and of regulatory beta subunits. KCNE4 beta subunit modulates the gating kinetics and enhances stability of the channel complex. Associates with KCNQ1/KVLTQ1 alpha subunit to inhibit potassium currents.; [Isoform 2]: May inhibit KCNQ4-mediated potassium currents.

**Summary**, from NCBI Gene [23704](https://www.ncbi.nlm.nih.gov/gene/23704):

> Voltage-gated potassium (Kv) channels represent the most complex class of voltage-gated ion channels from both functional and structural standpoints. Their diverse functions include regulating neurotransmitter release, heart rate, insulin secretion, neuronal excitability, epithelial electrolyte transport, smooth muscle contraction, and cell volume. This gene encodes a member of the potassium channel, voltage-gated, isk-related subfamily. This member is a type I membrane protein, and a beta …

**Accessions** — [HGNC:6244](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6244) · Entrez [23704](https://www.ncbi.nlm.nih.gov/gene/23704) · UniProt [Q8WWG9](https://www.uniprot.org/uniprotkb/Q8WWG9) · Ensembl [ENSG00000152049](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152049)

## Data

Gene col 7585: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7585); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7585, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7585]; `tensor/DDL_lfc|DDL_z.npy` [7585]; `embed/gene_vectors.npy` [7585]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7585 or target_col == 7585). Every well: [[KCNE4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNE4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
