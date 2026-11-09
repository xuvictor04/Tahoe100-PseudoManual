---
symbol: "LRFN2"
type: "gene"
col: 7997
ensembl_id: "ENSG00000156564"
name: "leucine rich repeat and fibronectin type III domain containing 2"
location: "6p21.2-p21.1"
module: 9
arm: "+"
pooled_cpm: 2.22
n_lines_expressing: 15
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 21
direction_downstream: 7
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# LRFN2

*leucine rich repeat and fibronectin type III domain containing 2* — 6p21.2-p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.24× (z +10.8, q 3e-24, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.46× (z +9.9, q 8e-21, up in 0 of 2 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.121×); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.0931×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.216×); [[Digitoxin (drug)]] 0.5 µM in 1 line (SHP-77 0.105×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRRM4]] (+0.95, fdr 7e-06), [[RIT2]] (+0.95, fdr 7e-06), [[SYT4]] (+0.94, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[CALCA]] → it (grade C ⚠); 7 go from it, the strongest it → [[MAN1C1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7997.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.24×** | +10.8 | 3e-24 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.46×** | +9.9 | 8e-21 | 0/2 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.17×** | +9.3 | 3e-18 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.38×** | +8.8 | 2e-16 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.42×** | +7.1 | 2e-10 | 2/4 (C32, BT-474) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.24×** | +6.4 | 1e-08 | 3/8 (A-427, BT-474, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.18×** | +4.4 | 9e-04 | 0/2 | inconsistent across doses | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.09×** | +4.0 | 0.004 | 0/1 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.02×** | +4.0 | 0.004 | 0/1 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.55×** | +3.8 | 0.010 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +3.7 | 0.013 | 0/1 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +3.5 | 0.020 | 0/1 | top dose only | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.55×** | +3.5 | 0.020 | 2/9 (NCI-H23, A-427) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.58×** | +3.4 | 0.031 | 0/1 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +3.3 | 0.039 | 0/2 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | **1.49×** | +3.2 | 0.045 | 0/6 | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +3.2 | 0.045 | 0/1 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.70×** | +3.0 | 0.084 | 0/5 | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.121×); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.0931×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.216×); [[Digitoxin (drug)]] 0.5 µM in 1 line (SHP-77 0.105×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7997. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 99.4 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.121× (z -14.8) |
| [[A-172 (line)]] | wt | 0.357 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.672 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.306 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.341 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.928 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.382 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.772 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.695 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.533 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.554 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.378 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.483 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.360 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.452 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.441 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.342 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.340 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.354 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.334 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.454 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.649 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.331 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.380 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.382 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.778 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.575 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.690 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.379 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7997), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRRM4]] | +0.95 | +0.91 / +0.92 | both halves | 7e-06 | **novel candidate** |
| [[RIT2]] | +0.95 | +0.96 / +0.91 | both halves | 7e-06 | **novel candidate** |
| [[SYT4]] | +0.94 | +0.96 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[ASCL1]] | +0.93 | +0.94 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[GRIK1]] | +0.87 | +0.88 / +0.81 | both halves | 7e-06 | pathway: Neuronal System |
| [[KCNB2]] | +0.87 | +0.84 / +0.86 | both halves | 7e-06 | pathway: Neuronal System |
| [[LINC02197]] | +0.84 | +0.82 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[CGA]] | +0.83 | +0.80 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[CALCA]] | +0.81 | +0.89 / +0.43 | both halves | 3e-05 | **novel candidate** |
| [[PCSK1]] | +0.79 | +0.80 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[RUNX1T1]] | +0.79 | +0.76 / +0.79 | both halves | 7e-06 |  |
| [[NELL1]] | +0.79 | +0.77 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 0, C 21. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALCA]] | C | CALCA activity raises LRFN2's level | lines that do not express CALCA (45) vs lines expressing it (5) | 4.11× lower at baseline in the lines without CALCA | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2; co-absent with the target |
| [[SSX1]] | C | SSX1 activity raises LRFN2's level | lines that do not express SSX1 (43) vs lines expressing it (7) | 3.15× lower at baseline in the lines without SSX1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00879, LINC02099, RNF17; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises LRFN2's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 3.26× lower at baseline in the lines without RIT2 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises LRFN2's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 3.26× lower at baseline in the lines without SYT4 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[KCNB2]] | C | KCNB2 activity raises LRFN2's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 2.75× lower at baseline in the lines without KCNB2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |
| [[CARD18]] | C | CARD18 activity raises LRFN2's level | lines that do not express CARD18 (44) vs lines expressing it (6) | 3.01× lower at baseline in the lines without CARD18 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000237031, APOB, BMP10; co-absent with the target |
| [[H19]] | C | H19 activity raises LRFN2's level | lines that do not express H19 (38) vs lines expressing it (12) | 1.81× lower at baseline in the lines without H19 | 0.024 | ⚠ within organs, on part of the lines; also absent: CALCA, SYT4, CGA; co-absent with the target |
| [[MIR3667HG]] | C | MIR3667HG activity raises LRFN2's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 1.98× lower at baseline in the lines without MIR3667HG | 0.028 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA; co-absent with the target |
| [[ASCL1]] | C | ASCL1 activity raises LRFN2's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 2.18× lower at baseline in the lines without ASCL1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[HGF]] | C | HGF activity raises LRFN2's level | lines that do not express HGF (38) vs lines expressing it (12) | 2.00× lower at baseline in the lines without HGF | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA; co-absent with the target |
| [[LINC01456]] | C | LINC01456 activity raises LRFN2's level | lines that do not express LINC01456 (42) vs lines expressing it (8) | 2.53× lower at baseline in the lines without LINC01456 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, CALCA, S100A8; co-absent with the target |
| [[PHYHIPL]] | C | PHYHIPL activity raises LRFN2's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 1.87× lower at baseline in the lines without PHYHIPL | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAN1C1]] | B | LRFN2 activity raises MAN1C1's level | lines that do not express LRFN2 (35) vs lines expressing it (15) | 3.04× lower at baseline in the lines without LRFN2 | 0.006 | ⚠ within organs, on part of the lines; also absent: MAGEA4, CALCA, PI15; maybe low, not absent |
| [[SEMA6D]] | B | LRFN2 activity raises SEMA6D's level | lines that do not express LRFN2 (35) vs lines expressing it (15) | 1.92× lower at baseline in the lines without LRFN2 | 0.041 | ⚠ within organs, on part of the lines; also absent: MAGEA4, CALCA, PI15; maybe low, not absent |
| [[LINC01250]] | B | LRFN2 activity raises LINC01250's level | lines that do not express LRFN2 (35) vs lines expressing it (15) | 2.12× lower at baseline in the lines without LRFN2 | 0.062 | ⚠ within organs, on part of the lines; also absent: MAGEA4, CALCA, PI15; maybe low, not absent |
| [[NELL1]] | B | LRFN2 activity raises NELL1's level | lines that do not express LRFN2 (35) vs lines expressing it (15) | 2.33× lower at baseline in the lines without LRFN2 | 0.089 | ⚠ within organs, on part of the lines; also absent: MAGEA4, CALCA, PI15; maybe low, not absent |
| [[RIMBP2]] | C | LRFN2 activity raises RIMBP2's level | lines that do not express LRFN2 (35) vs lines expressing it (15) | 1.66× lower at baseline in the lines without LRFN2 | 0.058 | ⚠ within organs, on part of the lines; also absent: MAGEA4, CALCA, PI15; maybe low, not absent; co-absent with the target |
| [[HGF]] | C | LRFN2 activity raises HGF's level | lines that do not express LRFN2 (35) vs lines expressing it (15) | 1.75× lower at baseline in the lines without LRFN2 | 0.063 | ⚠ within organs, on part of the lines; also absent: MAGEA4, CALCA, PI15; maybe low, not absent; co-absent with the target |
| [[CHST8]] | C | LRFN2 activity raises CHST8's level | lines that do not express LRFN2 (35) vs lines expressing it (15) | 4.29× lower at baseline in the lines without LRFN2 | 0.070 | ⚠ within organs, on part of the lines; also absent: MAGEA4, CALCA, PI15; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.712). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.7, 37.0); signed map (44.7, 34.2). **Vector** length 24.0, 9.45% of its response variance represented; |z| ≥ 3 in 166 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.1 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | +1.9 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.0 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.8 | -1.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat and fibronectin type III domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.2-p21.1 — chr6:40,391,591-40,587,364 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FIGLER2; previously KIAA1246, SALM1 |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; Ig-like cell adhesion molecule family |
| Reactome | 3 pathways, smallest: Synaptic adhesion-like molecules; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULH4](https://www.uniprot.org/uniprotkb/Q9ULH4) (Leucine-rich repeat and fibronectin type-III domain-containing protein 2):

> Promotes neurite outgrowth in hippocampal neurons. Enhances the cell surface expression of 2 NMDA receptor subunits GRIN1 and GRIN2A. May play a role in redistributing DLG4 to the cell periphery (By similarity).

**Summary**, from NCBI Gene [57497](https://www.ncbi.nlm.nih.gov/gene/57497):

> Predicted to be involved in modulation of chemical synaptic transmission and regulation of postsynapse organization. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21226](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21226) · Entrez [57497](https://www.ncbi.nlm.nih.gov/gene/57497) · UniProt [Q9ULH4](https://www.uniprot.org/uniprotkb/Q9ULH4) · Ensembl [ENSG00000156564](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156564)

## Data

Gene col 7997: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7997); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7997, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7997]; `tensor/DDL_lfc|DDL_z.npy` [7997]; `embed/gene_vectors.npy` [7997]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7997 or target_col == 7997). Every well: [[LRFN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRFN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
