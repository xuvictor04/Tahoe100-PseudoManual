---
symbol: "PDE1A"
type: "gene"
col: 3642
ensembl_id: "ENSG00000115252"
name: "phosphodiesterase 1A"
location: "2q32.1"
module: 19
arm: "+"
pooled_cpm: 13.83
n_lines_expressing: 12
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 16
direction_downstream: 26
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# PDE1A

*phosphodiesterase 1A* — 2q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.20× (z +16.5, q 0e+00, up in 4 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.0751×, NCI-H2030 0.299×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H460 0.0894×, NCI-H2030 0.130×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.119×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAX7]] (+0.83, fdr 7e-06), [[GLP2R]] (+0.81, fdr 7e-06), [[LINC03000]] (+0.81, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 26 go from it, the strongest it → [[PCDH15]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3642.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.20×** | +16.5 | 0e+00 | 4/6 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.97×** | +12.5 | 2e-33 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.76×** | +10.8 | 1e-24 | 1/4 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.38×** | +9.9 | 4e-21 | 4/7 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.65×** | +7.3 | 3e-11 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.22×** | +6.4 | 1e-08 | 2/8 (A-172, SK-MEL-2) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +6.1 | 1e-07 | 1/6 (A-172) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.64×** | +5.6 | 1e-06 | 2/9 (A-172, SNU-423) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +5.2 | 1e-05 | 0/5 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.081 | 3/7 (NCI-H460, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3642.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.0751×, NCI-H2030 0.299×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H460 0.0894×, NCI-H2030 0.130×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.119×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | 0.657× | -3.2 | 0.34 | 4/7 (NCI-H460, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.663× | -3.1 | 0.34 | 4/7 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.685× | -3.1 | 0.34 | 3/7 (NCI-H460, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3642. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 200 | 0 | 22 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0751× (z -17.5) |
| [[A-172 (line)]] | wt | 4.41 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 119× (z +20.8) | — |
| [[NCI-H2030 (line)]] | alt | 55.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.130× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 5.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.6× (z +12.5) | — |
| [[SNU-423 (line)]] | alt | 3.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.0× (z +11.9) | — |
| [[A-427 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.36 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.37 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.93 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.13 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3642), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAX7]] | +0.83 | +0.79 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[GLP2R]] | +0.81 | +0.78 / +0.78 | both halves | 7e-06 | pathway: G alpha (s) signalling events |
| [[LINC03000]] | +0.81 | +0.75 / +0.83 | both halves | 7e-06 |  |
| [[LINC01035]] | +0.80 | +0.73 / +0.84 | both halves | 7e-06 |  |
| [[SLC15A5]] | +0.80 | +0.78 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[SCARA5]] | +0.79 | +0.72 / +0.84 | both halves | 7e-06 |  |
| [[CHL1]] | +0.78 | +0.66 / +0.82 | both halves | 7e-06 |  |
| [[DPP10]] | +0.77 | +0.70 / +0.81 | both halves | 7e-06 |  |
| [[ADGRD1]] | +0.76 | +0.70 / +0.78 | both halves | 7e-06 |  |
| [[CTNND2]] | +0.74 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[GTF2I-AS1]] | +0.73 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[TBXT]] ⚠ | +0.73 | +0.63 / +0.79 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[CDH7]] | +0.72 | +0.66 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 2, C 14. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PDE1A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers PDE1A's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[GDA]] | C | GDA activity raises PDE1A's level | lines that do not express GDA (35) vs lines expressing it (15) | 1.82× lower at baseline in the lines without GDA | 0.015 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4; co-absent with the target |
| [[MARCOL]], [[SPINK13]] | C | MARCOL, SPINK13 activity raises PDE1A's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 4.08× lower at baseline in the lines without MARCOL, SPINK13 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[GSG1L2]] | C | GSG1L2 activity raises PDE1A's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 4.37× lower at baseline in the lines without GSG1L2 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |
| [[GTF2I-AS1]] | C | GTF2I-AS1 activity raises PDE1A's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 3.30× lower at baseline in the lines without GTF2I-AS1 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[LINC02945]] | C | LINC02945 activity raises PDE1A's level | lines that do not express LINC02945 (38) vs lines expressing it (12) | 2.50× lower at baseline in the lines without LINC02945 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02211, ENSG00000285751, ENSG00000275016; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises PDE1A's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 3.50× lower at baseline in the lines without LINC03000 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |
| [[GPRIN3]] | C | GPRIN3 activity raises PDE1A's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 2.00× lower at baseline in the lines without GPRIN3 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031; co-absent with the target |
| [[LINC02211]] | C | LINC02211 activity raises PDE1A's level | lines that do not express LINC02211 (38) vs lines expressing it (12) | 2.46× lower at baseline in the lines without LINC02211 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02945, LINC01035, PSG5; co-absent with the target |
| [[GREM2]] | C | GREM2 activity raises PDE1A's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 2.45× lower at baseline in the lines without GREM2 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054; co-absent with the target |
| [[SCARA5]] | C | SCARA5 activity raises PDE1A's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 2.76× lower at baseline in the lines without SCARA5 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 4, C 22. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDH15]] | B | PDE1A activity raises PCDH15's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 2.31× lower at baseline in the lines without PDE1A | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent |
| [[LSAMP]] | B | PDE1A activity raises LSAMP's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 2.49× lower at baseline in the lines without PDE1A | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent |
| [[IQCM]] | B | PDE1A activity raises IQCM's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 2.71× lower at baseline in the lines without PDE1A | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent |
| [[KCNMB2]] | B | PDE1A activity raises KCNMB2's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 2.94× lower at baseline in the lines without PDE1A | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent |
| [[ENPEP]] | C | PDE1A activity raises ENPEP's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 2.37× lower at baseline in the lines without PDE1A | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent; co-absent with the target |
| [[GREM2]] | C | PDE1A activity raises GREM2's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 3.20× lower at baseline in the lines without PDE1A | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent; co-absent with the target |
| [[NLGN4Y]] | C | PDE1A activity raises NLGN4Y's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 4.02× lower at baseline in the lines without PDE1A | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent; co-absent with the target |
| [[KCNK2]] | C | PDE1A activity raises KCNK2's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 2.10× lower at baseline in the lines without PDE1A | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent; co-absent with the target |
| [[NCKAP5-AS2]] | C | PDE1A activity raises NCKAP5-AS2's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 2.12× lower at baseline in the lines without PDE1A | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent; co-absent with the target |
| [[EPB41L3]] | C | PDE1A activity raises EPB41L3's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 3.56× lower at baseline in the lines without PDE1A | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent; co-absent with the target |
| [[LINC01035]] | C | PDE1A activity raises LINC01035's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 3.30× lower at baseline in the lines without PDE1A | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent; co-absent with the target |
| [[LINC02945]] | C | PDE1A activity raises LINC02945's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 4.16× lower at baseline in the lines without PDE1A | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.810). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.7, 36.5); signed map (43.3, 43.7). **Vector** length 48.5, 21.8% of its response variance represented; |z| ≥ 3 in 273 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +16.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +12.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.0 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.6 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +5.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.0 | +1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.9 | +3.2 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -0.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -2.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -1.1 | -2.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.0 | -3.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | +0.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | -0.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | +0.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | phosphodiesterase 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.1 — chr2:182,139,968-182,523,359 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phosphodiesterases |
| Reactome | 17 pathways, smallest: Cam-PDE 1 activation; cGMP effects; Nitric oxide stimulates guanylate cyclase |
| Matched by | ensembl_id |

**Function**, from UniProt [P54750](https://www.uniprot.org/uniprotkb/P54750) (Dual specificity calcium/calmodulin-dependent 3',5'-cyclic nucleotide phosphodiesterase 1A):

> Calcium/calmodulin-dependent cyclic nucleotide phosphodiesterase with a dual specificity for the second messengers cGMP and cAMP, which are key regulators of many important physiological processes. Has a higher efficiency with cGMP compared to cAMP.

**Summary**, from NCBI Gene [5136](https://www.ncbi.nlm.nih.gov/gene/5136):

> Cyclic nucleotide phosphodiesterases (PDEs) play a role in signal transduction by regulating intracellular cyclic nucleotide concentrations through hydrolysis of cAMP and/or cGMP to their respective nucleoside 5-prime monophosphates. Members of the PDE1 family, such as PDE1A, are Ca(2+)/calmodulin (see CALM1; MIM 114180)-dependent PDEs (CaM-PDEs) that are activated by calmodulin in the presence of Ca(2+) (Michibata et al., 2001 [PubMed 11342109]; Fidock et al., 2002 [PubMed 11747989]).[supplied …

**Accessions** — [HGNC:8774](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8774) · Entrez [5136](https://www.ncbi.nlm.nih.gov/gene/5136) · UniProt [P54750](https://www.uniprot.org/uniprotkb/P54750) · Ensembl [ENSG00000115252](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115252)

## Data

Gene col 3642: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3642); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3642, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3642]; `tensor/DDL_lfc|DDL_z.npy` [3642]; `embed/gene_vectors.npy` [3642]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3642 or target_col == 3642). Every well: [[PDE1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDE1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
