---
symbol: "SLC15A5"
type: "gene"
col: 12072
ensembl_id: "ENSG00000188991"
name: "solute carrier family 15 member 5"
location: "12p12.3"
module: 19
arm: "+"
pooled_cpm: 2.18
n_lines_expressing: 6
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 13
direction_downstream: 31
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SLC15A5

*solute carrier family 15 member 5* — 12p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 8.65× (z +10.1, q 4e-21, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.53× (z +8.6, q 2e-15, up in 0 of 2 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 9 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.0411×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.0143×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.105×); [[Belinostat (drug)]] 5 µM in 1 line (NCI-H460 0.0637×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCARA5]] (+0.90, fdr 7e-06), [[PAX7]] (+0.90, fdr 7e-06), [[LINC03000]] (+0.84, fdr 7e-06); moves opposite to [[ADRA2C]] (-0.53, fdr 1e-05), [[NPTX1]] (-0.48, fdr 3e-05), [[CCL3]] (-0.48, fdr 9e-04, ⚠ one half only (not replicated)), [[COLEC12]] (-0.47, fdr 3e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[SPINK13]] → it (grade C ⚠); 31 go from it, the strongest it → [[PLAC4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12072.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.65×** | +10.1 | 4e-21 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.53×** | +8.6 | 2e-15 | 0/2 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.82×** | +7.9 | 5e-13 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.98×** | +7.8 | 1e-12 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **4.09×** | +6.8 | 1e-09 | 0/2 | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.42×** | +6.0 | 1e-07 | 0/2 | top dose only | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.61×** | +4.6 | 3e-04 | 0/1 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.58×** | +4.4 | 8e-04 | 0/1 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.30×** | +4.1 | 0.002 | 0/1 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.93×** | +3.7 | 0.011 | 2/2 (NCI-H460, NCI-H1573) | inconsistent across doses | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.09×** | +3.6 | 0.018 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +3.5 | 0.024 | 0/1 | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +3.4 | 0.028 | 0/2 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.02×** | +3.4 | 0.028 | 1/1 (NCI-H460) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **2.10×** | +3.4 | 0.028 | 1/2 (NCI-H460) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.01×** | +3.2 | 0.052 | 1/1 (NCI-H460) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.49×** | +3.1 | 0.053 | 0/1 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.57×** | +3.0 | 0.073 | 0/2 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.85×** | +3.0 | 0.087 | 2/2 (NCI-H460, NCI-H1573) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12072.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 9 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.0411×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.0143×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.105×); [[Belinostat (drug)]] 5 µM in 1 line (NCI-H460 0.0637×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Erlotinib (drug)]] 0.05 µM |  | 0.456× | -3.6 | 0.12 | 0/2 | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.462× | -3.5 | 0.12 | 0/2 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12072. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 37.5 | 0 | 18 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0411× (z -20.0) |
| [[A-172 (line)]] | wt | 0.328 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.245 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.442 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.300 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.617 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.335 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.328 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.286 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.463 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.380 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.330 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.296 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.541 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.312 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.409 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.321 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.691 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.270 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.322 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.289 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.286 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.302 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.330 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.269 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.360 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.334 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.778 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.322 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.440 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.302 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12072), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCARA5]] | +0.90 | +0.92 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[PAX7]] | +0.90 | +0.92 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[LINC03000]] | +0.84 | +0.86 / +0.78 | both halves | 7e-06 |  |
| [[CHL1]] | +0.83 | +0.84 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[PDE1A]] | +0.80 | +0.78 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[DPP10]] | +0.79 | +0.80 / +0.71 | both halves | 7e-06 |  |
| [[LINC01035]] | +0.79 | +0.79 / +0.76 | both halves | 7e-06 |  |
| [[ADGRD1]] | +0.78 | +0.77 / +0.76 | both halves | 7e-06 |  |
| [[GREM2]] | +0.77 | +0.79 / +0.72 | both halves | 7e-06 |  |
| [[CTNND2]] | +0.76 | +0.81 / +0.66 | both halves | 7e-06 |  |
| [[GTF2I-AS1]] | +0.76 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[GLP2R]] | +0.76 | +0.80 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADRA2C]] | -0.53 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[NPTX1]] | -0.48 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[CCL3]] | -0.48 | -0.58 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[SCG3]] | -0.48 | -0.55 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[COLEC12]] | -0.47 | -0.57 / -0.26 | both halves | 3e-04 |  |
| [[CHST8]] | -0.47 | -0.50 / -0.29 | both halves | 3e-04 |  |
| [[CYB5R2]] | -0.45 | -0.51 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 0, C 13. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPINK13]] | C | SPINK13 activity raises SLC15A5's level | lines that do not express SPINK13 (45) vs lines expressing it (5) | 2.69× lower at baseline in the lines without SPINK13 | 0.009 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target |
| [[GTF2I-AS1]] | C | GTF2I-AS1 activity raises SLC15A5's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 2.53× lower at baseline in the lines without GTF2I-AS1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[GSG1L2]] | C | GSG1L2 activity raises SLC15A5's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 3.00× lower at baseline in the lines without GSG1L2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises SLC15A5's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 2.53× lower at baseline in the lines without LINC03000 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |
| [[SCARA5]] | C | SCARA5 activity raises SLC15A5's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 2.17× lower at baseline in the lines without SCARA5 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[CHL1]] | C | CHL1 activity raises SLC15A5's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 2.02× lower at baseline in the lines without CHL1 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168; co-absent with the target |
| [[AKR1B10]] | C | AKR1B10 activity raises SLC15A5's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 1.72× lower at baseline in the lines without AKR1B10 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[TBXT]] | C | TBXT activity raises SLC15A5's level | lines that do not express TBXT (47) vs lines expressing it (3) | 5.35× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |
| [[NLGN4Y]] | C | NLGN4Y activity raises SLC15A5's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 1.51× lower at baseline in the lines without NLGN4Y | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[CTNND2]] | C | CTNND2 activity raises SLC15A5's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 1.77× lower at baseline in the lines without CTNND2 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent; co-absent with the target |
| [[GDA]] | C | GDA activity raises SLC15A5's level | lines that do not express GDA (35) vs lines expressing it (15) | 1.37× lower at baseline in the lines without GDA | 0.088 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4; co-absent with the target |
| [[LINC01508]] | C | LINC01508 activity raises SLC15A5's level | lines that do not express LINC01508 (42) vs lines expressing it (8) | 1.84× lower at baseline in the lines without LINC01508 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, SPINK13, RHEX; co-absent with the target |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 5, C 26. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAC4]] | B | SLC15A5 activity raises PLAC4's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 3.77× lower at baseline in the lines without SLC15A5 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent |
| [[SPDYE10]] | B | SLC15A5 activity raises SPDYE10's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 2.24× lower at baseline in the lines without SLC15A5 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent |
| [[PART1]] | B | SLC15A5 activity raises PART1's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 2.19× lower at baseline in the lines without SLC15A5 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent |
| [[SOX6]] | B | SLC15A5 activity raises SOX6's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 3.07× lower at baseline in the lines without SLC15A5 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent |
| [[PCDH15]] | B | SLC15A5 activity raises PCDH15's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 2.50× lower at baseline in the lines without SLC15A5 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent |
| [[LINC03000]] | C | SLC15A5 activity raises LINC03000's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 6.77× lower at baseline in the lines without SLC15A5 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent; co-absent with the target |
| [[TBXT]] | C | SLC15A5 activity raises TBXT's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 5.81× lower at baseline in the lines without SLC15A5 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent; co-absent with the target |
| [[CHL1]] | C | SLC15A5 activity raises CHL1's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 5.10× lower at baseline in the lines without SLC15A5 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent; co-absent with the target |
| [[GTF2I-AS1]] | C | SLC15A5 activity raises GTF2I-AS1's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 4.31× lower at baseline in the lines without SLC15A5 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent; co-absent with the target |
| [[ADGRD1]] | C | SLC15A5 activity raises ADGRD1's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 5.69× lower at baseline in the lines without SLC15A5 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent; co-absent with the target |
| [[SCARA5]] | C | SLC15A5 activity raises SCARA5's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 4.00× lower at baseline in the lines without SLC15A5 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent; co-absent with the target |
| [[LINC01035]] | C | SLC15A5 activity raises LINC01035's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 6.56× lower at baseline in the lines without SLC15A5 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.696). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.0, 36.6); signed map (43.4, 44.0). **Vector** length 30.0, 30.4% of its response variance represented; |z| ≥ 3 in 78 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Budesonide (drug)]] 0.05 µM |  | +0.6 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.6 | +3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.6 | +2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.5 | +2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +0.5 | +8.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +0.5 | +1.8 |
| fall | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.4 | -1.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.4 | -1.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -0.4 | +6.0 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -0.3 | -0.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.3 | -0.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.3 | -2.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | -0.3 | +0.2 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | -0.3 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 15 member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.3 — chr12:16,188,485-16,277,685 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Solute carrier family 15 |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NIM6](https://www.uniprot.org/uniprotkb/A6NIM6) (Solute carrier family 15 member 5):

> Proton oligopeptide cotransporter.

**Summary**, from NCBI Gene [729025](https://www.ncbi.nlm.nih.gov/gene/729025):

> Predicted to enable transmembrane transporter activity. Predicted to be involved in transmembrane transport. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33455](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33455) · Entrez [729025](https://www.ncbi.nlm.nih.gov/gene/729025) · UniProt [A6NIM6](https://www.uniprot.org/uniprotkb/A6NIM6) · Ensembl [ENSG00000188991](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188991)

## Data

Gene col 12072: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12072); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12072, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12072]; `tensor/DDL_lfc|DDL_z.npy` [12072]; `embed/gene_vectors.npy` [12072]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12072 or target_col == 12072). Every well: [[SLC15A5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC15A5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
