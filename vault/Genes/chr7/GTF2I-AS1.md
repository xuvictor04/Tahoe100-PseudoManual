---
symbol: "GTF2I-AS1"
type: "gene"
col: 13864
ensembl_id: "ENSG00000232729"
name: "GTF2I antisense RNA 1"
location: "7q11.23"
module: 19
arm: "+"
pooled_cpm: 58.89
n_lines_expressing: 6
n_dd_up: 4
n_dd_down: 6
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 19
direction_downstream: 38
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# GTF2I-AS1

*GTF2I antisense RNA 1* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.40× (z +6.9, q 3e-09, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.43× (z +4.0, q 0.012, up in 0 of 4 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.548× (z -4.8, q 0.001, down in 3 of 3 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC03000]] (+0.79, fdr 7e-06), [[SPDYE10]] (+0.79, fdr 7e-06), [[SCARA5]] (+0.78, fdr 7e-06); moves opposite to [[ADRA2C]] (-0.48, fdr 3e-05), [[ELAVL2]] (-0.42, fdr 3e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 38 go from it, the strongest it → [[PLAC4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13864.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.40×** | +6.9 | 3e-09 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +4.5 | 0.002 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.0 | 0.012 | 0/4 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.55×** | +3.5 | 0.068 | 0/3 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.80× | +3.3 | 0.10 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.55× | +3.2 | 0.12 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 2.14× | +3.2 | 0.13 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | 1.50× | +3.1 | 0.15 | 0/3 | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | 1.47× | +3.0 | 0.15 | 0/3 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13864.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.548×** | -4.8 | 0.001 | 3/3 (NCI-H460, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.869× | -3.9 | 0.023 | 0/6 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.619×** | -3.7 | 0.043 | 2/3 (NCI-H460, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.636×** | -3.6 | 0.043 | 3/4 (NCI-H460, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.638×** | -3.6 | 0.043 | 2/3 (NCI-H460, A498) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.658×** | -3.3 | 0.088 | 2/3 (NCI-H460, A498) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.662×** | -3.3 | 0.090 | 2/4 (NCI-H460, A498) | all doses, stronger at high dose | position effect removed |
| [[Larotrectinib (drug)]] 5 µM |  | 0.763× | -3.0 | 0.16 | 2/4 (NCI-H460, A498) | top dose only | position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.662× | -3.0 | 0.16 | 0/3 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13864. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 889 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0182× (z -30.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0148× (z -22.9) |
| [[A498 (line)]] | wt | 161 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0482× (z -18.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.113× (z -12.9) |
| [[A-172 (line)]] | wt | 8.93 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.92 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.56 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.11 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.47 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 12.9 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.06 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.2 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.93 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.85 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.59 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.88 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.13 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.15 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 9.83 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.33 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 11.5 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.69 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.71 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.96 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 9.21 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.49 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 7.26 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 8.81 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.89 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.56 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.86 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.09 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.14 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.53 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 9.17 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 13.9 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 9.71 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13864), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC03000]] | +0.79 | +0.79 / +0.78 | both halves | 7e-06 |  |
| [[SPDYE10]] | +0.79 | +0.86 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[SCARA5]] | +0.78 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[LINC01508]] | +0.78 | +0.77 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[CHL1]] | +0.77 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[SLITRK4]] | +0.77 | +0.70 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[SLC15A5]] | +0.76 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[GLP2R]] | +0.76 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[PAX7]] | +0.75 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[CTNND2]] | +0.75 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[PDE1A]] | +0.73 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[LINC01035]] | +0.73 | +0.68 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADRA2C]] | -0.48 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[ELAVL2]] | -0.42 | -0.49 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 1, C 18. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises GTF2I-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GSG1L2]] | C | GSG1L2 activity raises GTF2I-AS1's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 5.98× lower at baseline in the lines without GSG1L2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |
| [[SPINK13]] | C | SPINK13 activity raises GTF2I-AS1's level | lines that do not express SPINK13 (45) vs lines expressing it (5) | 4.28× lower at baseline in the lines without SPINK13 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises GTF2I-AS1's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 4.57× lower at baseline in the lines without LINC03000 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |
| [[SLC15A5]] | C | SLC15A5 activity raises GTF2I-AS1's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 4.31× lower at baseline in the lines without SLC15A5 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent; co-absent with the target |
| [[CHL1]] | C | CHL1 activity raises GTF2I-AS1's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 3.17× lower at baseline in the lines without CHL1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168; co-absent with the target |
| [[SCARA5]] | C | SCARA5 activity raises GTF2I-AS1's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 3.39× lower at baseline in the lines without SCARA5 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[GREM2]] | C | GREM2 activity raises GTF2I-AS1's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 2.56× lower at baseline in the lines without GREM2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054; co-absent with the target |
| [[CTNND2]] | C | CTNND2 activity raises GTF2I-AS1's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 2.42× lower at baseline in the lines without CTNND2 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent; co-absent with the target |
| [[NLGN4Y]] | C | NLGN4Y activity raises GTF2I-AS1's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 1.79× lower at baseline in the lines without NLGN4Y | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[DPP10]] | C | DPP10 activity raises GTF2I-AS1's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 2.50× lower at baseline in the lines without DPP10 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[LINC01508]] | C | LINC01508 activity raises GTF2I-AS1's level | lines that do not express LINC01508 (42) vs lines expressing it (8) | 3.56× lower at baseline in the lines without LINC01508 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, SPINK13, RHEX; co-absent with the target |

### Downstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 5, C 33. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAC4]] | B | GTF2I-AS1 activity raises PLAC4's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 3.56× lower at baseline in the lines without GTF2I-AS1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent |
| [[SPDYE10]] | B | GTF2I-AS1 activity raises SPDYE10's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 2.79× lower at baseline in the lines without GTF2I-AS1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent |
| [[MN1]] | B | GTF2I-AS1 activity raises MN1's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 2.94× lower at baseline in the lines without GTF2I-AS1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent |
| [[MFF]] | B | GTF2I-AS1 activity raises MFF's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 2.00× lower at baseline in the lines without GTF2I-AS1 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent |
| [[SLC16A4]] | B | GTF2I-AS1 activity raises SLC16A4's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 3.52× lower at baseline in the lines without GTF2I-AS1 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent |
| [[LINC03000]] | C | GTF2I-AS1 activity raises LINC03000's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 6.65× lower at baseline in the lines without GTF2I-AS1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[TBXT]] | C | GTF2I-AS1 activity raises TBXT's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 5.76× lower at baseline in the lines without GTF2I-AS1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[CHL1]] | C | GTF2I-AS1 activity raises CHL1's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 4.94× lower at baseline in the lines without GTF2I-AS1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[LINC01035]] | C | GTF2I-AS1 activity raises LINC01035's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 6.47× lower at baseline in the lines without GTF2I-AS1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[SCARA5]] | C | GTF2I-AS1 activity raises SCARA5's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 3.80× lower at baseline in the lines without GTF2I-AS1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[SLC15A5]] | C | GTF2I-AS1 activity raises SLC15A5's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 2.53× lower at baseline in the lines without GTF2I-AS1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[DPP10]] | C | GTF2I-AS1 activity raises DPP10's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 4.49× lower at baseline in the lines without GTF2I-AS1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.755). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.1, 36.6); signed map (42.9, 44.3). **Vector** length 36.6, 27.6% of its response variance represented; |z| ≥ 3 in 116 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.2 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +1.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.8 | +1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.7 | -0.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.5 | +4.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.5 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.5 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.5 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.5 | -0.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -2.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.0 | -3.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -1.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.6 | -0.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.6 | -1.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.6 | -2.4 |
|  | [[EX229 (drug)]] 5 µM |  | -0.6 | -0.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | GTF2I antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q11.23 — chr7:74,688,864-74,729,001 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55572](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55572) · Entrez [101926943](https://www.ncbi.nlm.nih.gov/gene/101926943) · Ensembl [ENSG00000232729](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232729)

## Data

Gene col 13864: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13864); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13864, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13864]; `tensor/DDL_lfc|DDL_z.npy` [13864]; `embed/gene_vectors.npy` [13864]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13864 or target_col == 13864). Every well: [[GTF2I-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF2I-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
