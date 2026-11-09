---
symbol: "GSG1L2"
type: "gene"
col: 13237
ensembl_id: "ENSG00000214978"
name: "GSG1 like 2"
location: "17p13.1"
module: 19
arm: "+"
pooled_cpm: 2.9
n_lines_expressing: 5
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 13
direction_downstream: 33
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# GSG1L2

*GSG1 like 2* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 9.78× (z +9.7, q 2e-19, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 5.68× (z +7.7, q 3e-12, up in 0 of 1 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.258×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBXT]] (+0.84, fdr 7e-06, ⚠ TBXT in the vector space only through flagged drug-doses), [[GLP2R]] (+0.74, fdr 7e-06, ⚠ same locus), [[LINC03000]] (+0.68, fdr 7e-06), [[LINC01035]] (+0.66, fdr 1e-05), [[CDH7]] (+0.64, fdr 2e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[MARCOL]] → it (grade C ⚠); 33 go from it, the strongest it → [[SPDYE10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13237.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **9.78×** | +9.7 | 2e-19 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.83×** | +7.8 | 2e-12 | 1/1 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **5.68×** | +7.7 | 3e-12 | 0/1 | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.75×** | +6.4 | 3e-08 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.31×** | +5.2 | 2e-05 | 0/1 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.01×** | +4.4 | 0.001 | 0/1 | top dose only | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.96×** | +4.2 | 0.002 | 1/1 (NCI-H460) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.55×** | +4.0 | 0.005 | 0/1 | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.30×** | +3.8 | 0.011 | 0/1 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.24×** | +3.5 | 0.023 | 0/1 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **3.05×** | +3.5 | 0.023 | 1/1 (NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +3.2 | 0.069 | 0/1 | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.65×** | +3.1 | 0.088 | 0/1 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +3.1 | 0.088 | 0/1 | top dose only | cell-cycle shift (explains ~9% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.98×** | +3.0 | 0.098 | 0/1 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13237.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.258×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.507× | -3.0 | 0.64 | 1/1 (NCI-H460) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13237. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 51.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -8.7) |
| [[A-172 (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.319 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.347 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.312 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.788 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.401 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.505 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.375 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.389 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.395 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.361 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.517 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.504 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.492 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.362 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.406 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.299 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.517 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.375 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.368 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.782 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.404 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.613 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.482 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.354 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13237), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 5 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBXT]] ⚠ | +0.84 | +0.89 / +0.82 | both halves | 7e-06 | **novel candidate**; ⚠ in the vector space only through flagged drug-doses |
| [[GLP2R]] | +0.74 | +0.71 / +0.76 | both halves | 7e-06 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[LINC03000]] | +0.68 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[LINC01035]] | +0.66 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[CDH7]] | +0.64 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[CDH19]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 | **novel candidate** |
| [[LINC02994]] | +0.58 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[RSPO3]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[AKR1C2]] | +0.57 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[THSD7A]] | +0.55 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[ZSCAN31]] | +0.54 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[ADGRD1]] | +0.54 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[PAX7]] | +0.54 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[KIAA0319]] | +0.53 | +0.45 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 0, C 13. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MARCOL]] | C | MARCOL activity raises GSG1L2's level | lines that do not express MARCOL (45) vs lines expressing it (5) | 2.97× lower at baseline in the lines without MARCOL | 0.008 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target |
| [[ZNF736P9Y]] | C | ZNF736P9Y activity raises GSG1L2's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 1.75× lower at baseline in the lines without ZNF736P9Y | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364; co-absent with the target |
| [[GTF2I-AS1]] | C | GTF2I-AS1 activity raises GSG1L2's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 2.70× lower at baseline in the lines without GTF2I-AS1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises GSG1L2's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 2.76× lower at baseline in the lines without LINC03000 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |
| [[SCARA5]] | C | SCARA5 activity raises GSG1L2's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 2.34× lower at baseline in the lines without SCARA5 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[SLC15A5]] | C | SLC15A5 activity raises GSG1L2's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 2.72× lower at baseline in the lines without SLC15A5 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent; co-absent with the target |
| [[CHL1]] | C | CHL1 activity raises GSG1L2's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 2.14× lower at baseline in the lines without CHL1 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168; co-absent with the target |
| [[TBXT]] | C | TBXT activity raises GSG1L2's level | lines that do not express TBXT (47) vs lines expressing it (3) | 6.23× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |
| [[HOPX]] | C | HOPX activity raises GSG1L2's level | lines that do not express HOPX (42) vs lines expressing it (8) | 2.06× lower at baseline in the lines without HOPX | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SERPINB11, TBXT, GSG1L2; co-absent with the target |
| [[CTNND2]] | C | CTNND2 activity raises GSG1L2's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 1.85× lower at baseline in the lines without CTNND2 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent; co-absent with the target |
| [[KCNE4]] | C | KCNE4 activity raises GSG1L2's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 1.46× lower at baseline in the lines without KCNE4 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN; co-absent with the target |
| [[LINC01508]] | C | LINC01508 activity raises GSG1L2's level | lines that do not express LINC01508 (42) vs lines expressing it (8) | 1.95× lower at baseline in the lines without LINC01508 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, SPINK13, RHEX; co-absent with the target |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 7, C 26. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPDYE10]] | B | GSG1L2 activity raises SPDYE10's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 2.63× lower at baseline in the lines without GSG1L2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000 |
| [[PCDH15]] | B | GSG1L2 activity raises PCDH15's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 3.09× lower at baseline in the lines without GSG1L2 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000 |
| [[LSAMP]] | B | GSG1L2 activity raises LSAMP's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 2.61× lower at baseline in the lines without GSG1L2 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000 |
| [[SOX6]] | B | GSG1L2 activity raises SOX6's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 4.47× lower at baseline in the lines without GSG1L2 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000 |
| [[MN1]] | B | GSG1L2 activity raises MN1's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 3.70× lower at baseline in the lines without GSG1L2 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000 |
| [[KIAA0825]] | B | GSG1L2 activity raises KIAA0825's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 3.55× lower at baseline in the lines without GSG1L2 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000 |
| [[KCNMB2]] | B | GSG1L2 activity raises KCNMB2's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 4.37× lower at baseline in the lines without GSG1L2 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000 |
| [[LINC03000]] | C | GSG1L2 activity raises LINC03000's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 10.25× lower at baseline in the lines without GSG1L2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |
| [[TBXT]] | C | GSG1L2 activity raises TBXT's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 8.44× lower at baseline in the lines without GSG1L2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |
| [[LINC01035]] | C | GSG1L2 activity raises LINC01035's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 10.01× lower at baseline in the lines without GSG1L2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |
| [[CHL1]] | C | GSG1L2 activity raises CHL1's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 7.33× lower at baseline in the lines without GSG1L2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |
| [[GTF2I-AS1]] | C | GSG1L2 activity raises GTF2I-AS1's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 5.98× lower at baseline in the lines without GSG1L2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.571). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.1, 35.9); signed map (43.0, 43.1). **Vector** length 7.43, 5.59% of its response variance represented; |z| ≥ 3 in 18 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +0.4 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.4 | +9.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.3 | -0.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +0.3 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +0.3 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.2 | +1.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.2 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.2 | +0.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.2 | +1.7 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -0.2 | -0.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.2 | -1.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.2 | -0.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.2 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.2 | -0.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.2 | -0.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.2 | -1.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.2 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | GSG1 like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:9,800,608-9,822,079 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [A8MUP6](https://www.uniprot.org/uniprotkb/A8MUP6) carries no function annotation.

**Summary**, from NCBI Gene [644070](https://www.ncbi.nlm.nih.gov/gene/644070):

> Predicted to be located in membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:51826](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51826) · Entrez [644070](https://www.ncbi.nlm.nih.gov/gene/644070) · UniProt [A8MUP6](https://www.uniprot.org/uniprotkb/A8MUP6) · Ensembl [ENSG00000214978](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214978)

## Data

Gene col 13237: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13237); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13237, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13237]; `tensor/DDL_lfc|DDL_z.npy` [13237]; `embed/gene_vectors.npy` [13237]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13237 or target_col == 13237). Every well: [[GSG1L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSG1L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
