---
symbol: "TBXT"
type: "gene"
col: 8949
ensembl_id: "ENSG00000164458"
name: "T-box transcription factor T"
location: "6q27"
module: 19
arm: "+"
pooled_cpm: 25.56
n_lines_expressing: 3
n_dd_up: 4
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 22
direction_downstream: 38
tags: ["gene", "module/019", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# TBXT

*T-box transcription factor T* — 6q27

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.49× (z +7.7, q 8e-12, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.257×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLP2R]] (+0.88, fdr 7e-06), [[LINC03000]] (+0.87, fdr 7e-06), [[LINC01035]] (+0.85, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[GSG1L2]] → it (grade C ⚠); 38 go from it, the strongest it → [[LINC03000]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8949.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.49×** | +7.7 | 8e-12 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.93×** | +6.7 | 4e-09 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.45×** | +4.6 | 9e-04 | 0/1 | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.45×** | +4.2 | 0.003 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8949.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.257×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.483× | -3.5 | 0.26 | 0/1 | inconsistent across doses |  |
| [[Futibatinib (drug)]] 0.05 µM |  | 0.509× | -3.3 | 0.26 | 0/1 | inconsistent across doses | position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.526× | -3.1 | 0.29 | 0/1 | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.651× | -3.1 | 0.29 | 0/1 | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.534× | -3.0 | 0.29 | 0/1 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.70 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8949. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 477 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -10.0) |
| [[A-172 (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.11 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.69 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.34 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.36 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.26 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.09 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.81 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8949), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLP2R]] | +0.88 | +0.85 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[LINC03000]] | +0.87 | +0.77 / +0.92 | both halves | 7e-06 | **novel candidate** |
| [[LINC01035]] | +0.85 | +0.65 / +0.91 | both halves | 7e-06 | **novel candidate** |
| [[GSG1L2]] | +0.84 | +0.89 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[CHL1]] | +0.77 | +0.61 / +0.85 | both halves | 7e-06 |  |
| [[ADGRD1]] | +0.77 | +0.60 / +0.83 | both halves | 7e-06 |  |
| [[SCARA5]] | +0.75 | +0.63 / +0.86 | both halves | 7e-06 |  |
| [[DPP10]] | +0.75 | +0.58 / +0.84 | both halves | 7e-06 |  |
| [[PAX7]] | +0.75 | +0.65 / +0.75 | both halves | 7e-06 | pathway: Gastrulation |
| [[GREM2]] | +0.75 | +0.61 / +0.78 | both halves | 7e-06 |  |
| [[PDE1A]] | +0.73 | +0.63 / +0.79 | both halves | 7e-06 |  |
| [[CDH7]] | +0.72 | +0.61 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 0, C 22. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GSG1L2]] | C | GSG1L2 activity raises TBXT's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 8.44× lower at baseline in the lines without GSG1L2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |
| [[GTF2I-AS1]] | C | GTF2I-AS1 activity raises TBXT's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 5.76× lower at baseline in the lines without GTF2I-AS1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[MARCOL]], [[SPINK13]] | C | MARCOL, SPINK13 activity raises TBXT's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 5.87× lower at baseline in the lines without MARCOL, SPINK13 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[ZNF736P9Y]] | C | ZNF736P9Y activity raises TBXT's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 2.53× lower at baseline in the lines without ZNF736P9Y | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises TBXT's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 6.18× lower at baseline in the lines without LINC03000 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |
| [[SLC15A5]] | C | SLC15A5 activity raises TBXT's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 5.81× lower at baseline in the lines without SLC15A5 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent; co-absent with the target |
| [[GREM2]] | C | GREM2 activity raises TBXT's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 3.35× lower at baseline in the lines without GREM2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054; co-absent with the target |
| [[SCARA5]] | C | SCARA5 activity raises TBXT's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 4.41× lower at baseline in the lines without SCARA5 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[CHL1]] | C | CHL1 activity raises TBXT's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 3.90× lower at baseline in the lines without CHL1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168; co-absent with the target |
| [[CTNND2]] | C | CTNND2 activity raises TBXT's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 3.01× lower at baseline in the lines without CTNND2 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent; co-absent with the target |
| [[AKR1B10]] | C | AKR1B10 activity raises TBXT's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 2.56× lower at baseline in the lines without AKR1B10 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[HOPX]] | C | HOPX activity raises TBXT's level | lines that do not express HOPX (42) vs lines expressing it (8) | 3.22× lower at baseline in the lines without HOPX | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SERPINB11, TBXT, GSG1L2; co-absent with the target |

### Downstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 0, C 38. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC03000]] | C | TBXT activity raises LINC03000's level | lines that do not express TBXT (47) vs lines expressing it (3) | 25.07× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |
| [[LINC01035]] | C | TBXT activity raises LINC01035's level | lines that do not express TBXT (47) vs lines expressing it (3) | 24.81× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |
| [[CHL1]] | C | TBXT activity raises CHL1's level | lines that do not express TBXT (47) vs lines expressing it (3) | 17.71× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |
| [[ADGRD1]] | C | TBXT activity raises ADGRD1's level | lines that do not express TBXT (47) vs lines expressing it (3) | 15.89× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |
| [[PDE3A]] | C | TBXT activity raises PDE3A's level | lines that do not express TBXT (47) vs lines expressing it (3) | 15.31× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |
| [[DPP10]] | C | TBXT activity raises DPP10's level | lines that do not express TBXT (47) vs lines expressing it (3) | 14.48× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |
| [[GTF2I-AS1]] | C | TBXT activity raises GTF2I-AS1's level | lines that do not express TBXT (47) vs lines expressing it (3) | 13.02× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |
| [[GREM2]] | C | TBXT activity raises GREM2's level | lines that do not express TBXT (47) vs lines expressing it (3) | 12.54× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |
| [[PLAC4]] | C | TBXT activity raises PLAC4's level | lines that do not express TBXT (47) vs lines expressing it (3) | 11.59× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; its own permutation p |
| [[CTNND2]] | C | TBXT activity raises CTNND2's level | lines that do not express TBXT (47) vs lines expressing it (3) | 11.34× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |
| [[SCARA5]] | C | TBXT activity raises SCARA5's level | lines that do not express TBXT (47) vs lines expressing it (3) | 11.21× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |
| [[COL8A1]] | C | TBXT activity raises COL8A1's level | lines that do not express TBXT (47) vs lines expressing it (3) | 9.54× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.764). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (44.6, 36.2); signed map (43.2, 43.6). **Vector** length 13.8, 16.9% of its response variance represented; |z| ≥ 3 in 23 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.0 | +7.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.9 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.7 | +4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +0.4 | +1.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +0.4 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.4 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.4 | -0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.3 | +2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +0.3 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.3 | +2.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.5 | -2.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.3 | -1.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.3 | -1.3 |
|  | [[EX229 (drug)]] 5 µM |  | -0.3 | -0.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.3 | -1.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.3 | -1.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -0.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | T-box transcription factor T |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q27 — chr6:166,157,656-166,168,700 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously T |
| Gene groups (HGNC) | T-box transcription factors |
| Reactome | 7 pathways, smallest: Epithelial-Mesenchymal Transition (EMT) during gastrulation; Formation of definitive endoderm; Germ layer formation at gastrulation |
| Matched by | ensembl_id |

**Function**, from UniProt [O15178](https://www.uniprot.org/uniprotkb/O15178) (T-box transcription factor T):

> Involved in the transcriptional regulation of genes required for mesoderm formation and differentiation. Binds to a palindromic T site 5'-TTCACACCTAGGTGTGAA-3' DNA sequence and activates gene transcription when bound to such a site.

**Summary**, from NCBI Gene [6862](https://www.ncbi.nlm.nih.gov/gene/6862):

> The protein encoded by this gene is an embryonic nuclear transcription factor that binds to a specific DNA element, the palindromic T-site. It binds through a region in its N-terminus, called the T-box, and effects transcription of genes required for mesoderm formation and differentiation. The protein is localized to notochord-derived cells. Variation in this gene was associated with susceptibility to neural tube defects and chordoma. A mutation in this gene was found in a family with sacral …

**Accessions** — [HGNC:11515](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11515) · Entrez [6862](https://www.ncbi.nlm.nih.gov/gene/6862) · UniProt [O15178](https://www.uniprot.org/uniprotkb/O15178) · Ensembl [ENSG00000164458](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164458)

## Data

Gene col 8949: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8949); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8949, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8949]; `tensor/DDL_lfc|DDL_z.npy` [8949]; `embed/gene_vectors.npy` [8949]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8949 or target_col == 8949). Every well: [[TBXT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBXT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
