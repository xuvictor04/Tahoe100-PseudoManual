---
symbol: "GLP2R"
type: "gene"
col: 781
ensembl_id: "ENSG00000065325"
name: "glucagon like peptide 2 receptor"
location: "17p13.1"
module: 19
arm: "+"
pooled_cpm: 5.19
n_lines_expressing: 7
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 16
direction_downstream: 31
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# GLP2R

*glucagon like peptide 2 receptor* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.09× (z +9.2, q 1e-17, up in 2 of 4 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Rutin (trihydrate) (drug)]] 0.05 µM: 0.462× (z -4.1, q 0.020, down in 0 of 4 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.173×); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H460 0.138×; ⚠ cell-cycle shift, explains ~10% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H460 0.149×; ⚠ cell-cycle shift, explains ~27% of this change); [[Belinostat (drug)]] 5 µM in 1 line (NCI-H460 0.197×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC03000]] (+0.90, fdr 7e-06), [[TBXT]] (+0.88, fdr 7e-06, ⚠ TBXT in the vector space only through flagged drug-doses), [[PAX7]] (+0.86, fdr 7e-06), [[LINC01035]] (+0.84, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[MARCOL]], [[SPINK13]] → it (grade C ⚠); 31 go from it, the strongest it → [[PLAC4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 781.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.09×** | +9.2 | 1e-17 | 2/4 (SNU-423, HEC-1-A) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.65×** | +8.6 | 3e-15 | 0/1 | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.31×** | +7.8 | 1e-12 | 0/1 | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.81×** | +7.7 | 1e-12 | 0/2 | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +4.5 | 8e-04 | 1/4 (A549) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.13×** | +4.4 | 0.001 | 0/4 | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +4.1 | 0.003 | 1/2 (A549) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.56×** | +3.9 | 0.007 | 0/1 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.09×** | +3.4 | 0.038 | 0/1 | top dose only | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +3.4 | 0.038 | 0/1 | top dose only | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.3 | 0.054 | 1/4 (A549) | top dose only |  |
| [[Decitabine (drug)]] 0.5 µM |  | 1.68× | +3.0 | 0.12 | 0/4 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 781.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.173×); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H460 0.138×; ⚠ cell-cycle shift, explains ~10% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H460 0.149×; ⚠ cell-cycle shift, explains ~27% of this change); [[Belinostat (drug)]] 5 µM in 1 line (NCI-H460 0.197×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.462×** | -4.1 | 0.020 | 0/4 | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.544× | -3.3 | 0.22 | 0/4 | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.546× | -3.2 | 0.22 | 0/4 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 781. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 91.5 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -13.9) |
| [[A-172 (line)]] | wt | 0.863 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.368 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.556 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.655 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.661 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.780 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.498 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.785 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.548 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.798 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.450 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.381 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.877 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.906 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.738 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.843 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.581 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.553 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.490 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.637 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.540 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 781), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC03000]] | +0.90 | +0.87 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[TBXT]] ⚠ | +0.88 | +0.85 / +0.88 | both halves | 7e-06 | **novel candidate**; ⚠ in the vector space only through flagged drug-doses |
| [[PAX7]] | +0.86 | +0.84 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[LINC01035]] | +0.84 | +0.76 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[SCARA5]] | +0.82 | +0.81 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[PDE1A]] | +0.81 | +0.78 / +0.78 | both halves | 7e-06 | pathway: G alpha (s) signalling events |
| [[CHL1]] | +0.80 | +0.74 / +0.79 | both halves | 7e-06 |  |
| [[CTNND2]] | +0.80 | +0.78 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[ADGRD1]] | +0.79 | +0.72 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[GREM2]] | +0.79 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[COL4A6]] | +0.79 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[DPP10]] | +0.77 | +0.75 / +0.80 | both halves | 7e-06 |  |
| [[SPDYE10]] | +0.77 | +0.80 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 0, C 16. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MARCOL]], [[SPINK13]] | C | MARCOL, SPINK13 activity raises GLP2R's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 3.56× lower at baseline in the lines without MARCOL, SPINK13 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[ZNF736P9Y]] | C | ZNF736P9Y activity raises GLP2R's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 1.96× lower at baseline in the lines without ZNF736P9Y | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364; co-absent with the target |
| [[AKR1B10]] | C | AKR1B10 activity raises GLP2R's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 2.22× lower at baseline in the lines without AKR1B10 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[GTF2I-AS1]] | C | GTF2I-AS1 activity raises GLP2R's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 3.36× lower at baseline in the lines without GTF2I-AS1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[GSG1L2]] | C | GSG1L2 activity raises GLP2R's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 4.03× lower at baseline in the lines without GSG1L2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |
| [[NLGN4Y]] | C | NLGN4Y activity raises GLP2R's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 1.95× lower at baseline in the lines without NLGN4Y | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises GLP2R's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 3.18× lower at baseline in the lines without LINC03000 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |
| [[SCARA5]] | C | SCARA5 activity raises GLP2R's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 2.62× lower at baseline in the lines without SCARA5 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[TBXT]] | C | TBXT activity raises GLP2R's level | lines that do not express TBXT (47) vs lines expressing it (3) | 8.43× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |
| [[CTNND2]] | C | CTNND2 activity raises GLP2R's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 2.08× lower at baseline in the lines without CTNND2 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent; co-absent with the target |
| [[GREM2]] | C | GREM2 activity raises GLP2R's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 2.23× lower at baseline in the lines without GREM2 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054; co-absent with the target |
| [[SLC15A5]] | C | SLC15A5 activity raises GLP2R's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 3.13× lower at baseline in the lines without SLC15A5 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 5, C 26. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAC4]] | B | GLP2R activity raises PLAC4's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 3.04× lower at baseline in the lines without GLP2R | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054 |
| [[SLC16A4]] | B | GLP2R activity raises SLC16A4's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 2.20× lower at baseline in the lines without GLP2R | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054 |
| [[SLCO1C1]] | B | GLP2R activity raises SLCO1C1's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 1.73× lower at baseline in the lines without GLP2R | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054 |
| [[MN1]] | B | GLP2R activity raises MN1's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 3.00× lower at baseline in the lines without GLP2R | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054 |
| [[BMPER]] | B | GLP2R activity raises BMPER's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 3.87× lower at baseline in the lines without GLP2R | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054 |
| [[AKR1B10]] | C | GLP2R activity raises AKR1B10's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 3.29× lower at baseline in the lines without GLP2R | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054; co-absent with the target |
| [[NLGN4Y]] | C | GLP2R activity raises NLGN4Y's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 5.32× lower at baseline in the lines without GLP2R | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054; co-absent with the target |
| [[P3H2]] | C | GLP2R activity raises P3H2's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 3.87× lower at baseline in the lines without GLP2R | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054; co-absent with the target |
| [[LAMB4]] | C | GLP2R activity raises LAMB4's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 2.22× lower at baseline in the lines without GLP2R | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054; co-absent with the target |
| [[P3H2-AS1]] | C | GLP2R activity raises P3H2-AS1's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 2.24× lower at baseline in the lines without GLP2R | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054; co-absent with the target |
| [[PRICKLE1]] | C | GLP2R activity raises PRICKLE1's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 3.98× lower at baseline in the lines without GLP2R | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054; co-absent with the target |
| [[CDH19]] | C | GLP2R activity raises CDH19's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 3.25× lower at baseline in the lines without GLP2R | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.872). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.8, 36.2); signed map (43.0, 43.8). **Vector** length 20.4, 9.84% of its response variance represented; |z| ≥ 3 in 110 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.51 to 18).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.8 | +7.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.4 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.2 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.8 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.8 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.5 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.5 | +1.1 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -0.6 | -1.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -0.5 | -1.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.5 | -1.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.4 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.4 | -3.2 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -0.4 | -0.8 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | glucagon like peptide 2 receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:9,822,206-9,892,099 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Glucagon receptor family |
| Reactome | 6 pathways, smallest: Glucagon-type ligand receptors; Class B/2 (Secretin family receptors); G alpha (s) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [O95838](https://www.uniprot.org/uniprotkb/O95838) (Glucagon-like peptide 2 receptor):

> This is a receptor for glucagon-like peptide 2. The activity of this receptor is mediated by G proteins which activate adenylyl cyclase.

**Summary**, from NCBI Gene [9340](https://www.ncbi.nlm.nih.gov/gene/9340):

> This gene encodes a G protein-coupled receptor closely related to the glucagon receptor that binds glucagon-like peptide 2 (GLP-2). Activation of this gene stimulates intestinal growth by increasing villus height, enhancing crypt cell proliferation, and reducing enterocyte apoptosis, thereby promoting nutrient absorption and maintaining gut barrier integrity. Glucagon like protein 2 receptor signaling also regulates intestinal blood flow, supports mucosal healing after injury, and modulates gut …

**Accessions** — [HGNC:4325](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4325) · Entrez [9340](https://www.ncbi.nlm.nih.gov/gene/9340) · UniProt [O95838](https://www.uniprot.org/uniprotkb/O95838) · Ensembl [ENSG00000065325](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065325)

## Data

Gene col 781: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 781); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 781, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 781]; `tensor/DDL_lfc|DDL_z.npy` [781]; `embed/gene_vectors.npy` [781]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 781 or target_col == 781). Every well: [[GLP2R — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLP2R.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
