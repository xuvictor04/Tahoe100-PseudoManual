---
symbol: "KHDRBS2"
type: "gene"
col: 3338
ensembl_id: "ENSG00000112232"
name: "KH RNA binding domain containing, signal transduction associated 2"
location: "6q11.1"
module: 9
arm: "+"
pooled_cpm: 6.3
n_lines_expressing: 13
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 19
direction_downstream: 3
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# KHDRBS2

*KH RNA binding domain containing, signal transduction associated 2* — 6q11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.92× (z +17.0, q 0e+00, up in 2 of 5 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.375×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRFN2]] (+0.75, fdr 1e-05), [[SRRM4]] (+0.75, fdr 1e-05), [[GRIA2]] (+0.75, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[ASCL1]] → it (grade C ⚠); 3 go from it, the strongest it → [[AK4P3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3338.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.92×** | +17.0 | 0e+00 | 2/5 (NCI-H2030, SW 900) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.00×** | +10.1 | 2e-21 | 1/3 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.49×** | +9.4 | 7e-19 | 1/3 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.18×** | +8.3 | 1e-14 | 2/6 (NCI-H2347, NCI-H2030) | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.21×** | +8.1 | 5e-14 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.01×** | +7.4 | 1e-11 | 7/9 (NCI-H2030, NCI-H2347, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.60×** | +7.2 | 4e-11 | 5/8 (SK-MEL-2, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +4.5 | 4e-04 | 2/4 (SW 900, NCI-H2347) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.72×** | +3.8 | 0.010 | 0/4 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +3.3 | 0.050 | 4/7 (NCI-H2347, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.84×** | +3.3 | 0.050 | 0/7 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +3.2 | 0.050 | 1/6 (SW 900) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.28×** | +3.2 | 0.050 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.053 | 0/9 | top dose only |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.054 | 1/7 (NCI-H2030) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3338.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.375×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.652× | -3.1 | 0.38 | 2/8 (SW 900, A-427) | rises with dose | plate-row cell shift |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 0.655× | -3.1 | 0.38 | 0/8 | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.673× | -3.0 | 0.38 | 1/9 (SW 900) | inconsistent across doses |  |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.675× | -3.0 | 0.38 | 1/8 (SW 900) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3338. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 1.92 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 33.3× (z +11.7) | — |
| [[NCI-H2347 (line)]] | alt | 8.15 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.95× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 264 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -9.0) |
| [[A-172 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.27 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3338), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRFN2]] | +0.75 | +0.52 / +0.80 | both halves | 1e-05 |  |
| [[SRRM4]] | +0.75 | +0.51 / +0.78 | both halves | 1e-05 |  |
| [[GRIA2]] | +0.75 | +0.61 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[KCNH7]] | +0.73 | +0.58 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[SYT4]] | +0.71 | +0.45 / +0.74 | both halves | 3e-05 |  |
| [[LINC02197]] | +0.70 | +0.51 / +0.76 | both halves | 1e-05 |  |
| [[RIT2]] | +0.69 | +0.42 / +0.71 | both halves | 4e-05 |  |
| [[KCNB2]] | +0.68 | +0.45 / +0.75 | both halves | 3e-05 |  |
| [[ASCL1]] | +0.68 | +0.42 / +0.70 | both halves | 4e-05 |  |
| [[CGA]] | +0.68 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[KCTD8]] | +0.68 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[CDH12]] | +0.65 | +0.54 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 0, C 19. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASCL1]] | C | ASCL1 activity raises KHDRBS2's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 4.37× lower at baseline in the lines without ASCL1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[LINC02999]] | C | LINC02999 activity raises KHDRBS2's level | lines that do not express LINC02999 (43) vs lines expressing it (7) | 5.60× lower at baseline in the lines without LINC02999 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, GCG, SFTPA2; co-absent with the target |
| [[SRRM4]] | C | SRRM4 activity raises KHDRBS2's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 3.53× lower at baseline in the lines without SRRM4 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent; co-absent with the target |
| [[AK4P3]] | C | AK4P3 activity raises KHDRBS2's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 2.50× lower at baseline in the lines without AK4P3 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF; co-absent with the target |
| [[RUNX1T1]] | C | RUNX1T1 activity raises KHDRBS2's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 3.01× lower at baseline in the lines without RUNX1T1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |
| [[SNTG1]] | C | SNTG1 activity raises KHDRBS2's level | lines that do not express SNTG1 (38) vs lines expressing it (12) | 3.14× lower at baseline in the lines without SNTG1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[RMST]] | C | RMST activity raises KHDRBS2's level | lines that do not express RMST (35) vs lines expressing it (15) | 2.33× lower at baseline in the lines without RMST | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, ENSG00000287923; maybe low, not absent; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises KHDRBS2's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 4.99× lower at baseline in the lines without SYT4 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[CALCA]] | C | CALCA activity raises KHDRBS2's level | lines that do not express CALCA (45) vs lines expressing it (5) | 4.96× lower at baseline in the lines without CALCA | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2; co-absent with the target |
| [[SSX1]] | C | SSX1 activity raises KHDRBS2's level | lines that do not express SSX1 (43) vs lines expressing it (7) | 2.72× lower at baseline in the lines without SSX1 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00879, LINC02099, RNF17; co-absent with the target |
| [[LINC02506]] | C | LINC02506 activity raises KHDRBS2's level | lines that do not express LINC02506 (40) vs lines expressing it (10) | 3.31× lower at baseline in the lines without LINC02506 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OVAAL, LINC01610, ENSG00000241168; co-absent with the target |
| [[CCDC144NL-AS1]] | C | CCDC144NL-AS1 activity raises KHDRBS2's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 2.11× lower at baseline in the lines without CCDC144NL-AS1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AK4P3]] | C | KHDRBS2 activity raises AK4P3's level | lines that do not express KHDRBS2 (37) vs lines expressing it (13) | 3.25× lower at baseline in the lines without KHDRBS2 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[DACH1]] | C | KHDRBS2 activity raises DACH1's level | lines that do not express KHDRBS2 (37) vs lines expressing it (13) | 3.01× lower at baseline in the lines without KHDRBS2 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[GRIA2]] | C | KHDRBS2 activity raises GRIA2's level | lines that do not express KHDRBS2 (37) vs lines expressing it (13) | 3.14× lower at baseline in the lines without KHDRBS2 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.730). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.0, 36.4); signed map (43.5, 35.0). **Vector** length 21.4, 5.31% of its response variance represented; |z| ≥ 3 in 224 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.56 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +17.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.9 | +1.7 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.0 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -3.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -2.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | KH RNA binding domain containing, signal transduction associated 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q11.1 — chr6:61,679,961-62,286,225 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SLM1, SLM-1, MGC26664; previously KHDRBS2-OT1, KHDRBS2-OT |
| Gene groups (HGNC) | Signal transduction and activation of RNA metabolism family |
| Reactome | 3 pathways, smallest: PTK6 Regulates Proteins Involved in RNA Processing; Signaling by Non-Receptor Tyrosine Kinases; Signaling by PTK6 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VWX1](https://www.uniprot.org/uniprotkb/Q5VWX1) (KH domain-containing, RNA-binding, signal transduction-associated protein 2):

> RNA-binding protein that plays a role in the regulation of alternative splicing and influences mRNA splice site selection and exon inclusion. Binds both poly(A) and poly(U) homopolymers. Phosphorylation by PTK6 inhibits its RNA-binding ability (By similarity). Induces an increased concentration-dependent incorporation of exon in CD44 pre-mRNA by direct binding to purine-rich exonic enhancer. Can regulate alternative splicing of NRXN1 in the laminin G-like domain 6 containing the evolutionary …

**Summary**, from NCBI Gene [202559](https://www.ncbi.nlm.nih.gov/gene/202559):

> Predicted to enable mRNA binding activity and poly(A) binding activity. Predicted to be involved in regulation of alternative mRNA splicing, via spliceosome. Predicted to be located in nucleoplasm. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18114](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18114) · Entrez [202559](https://www.ncbi.nlm.nih.gov/gene/202559) · UniProt [Q5VWX1](https://www.uniprot.org/uniprotkb/Q5VWX1) · Ensembl [ENSG00000112232](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112232)

## Data

Gene col 3338: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3338); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3338, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3338]; `tensor/DDL_lfc|DDL_z.npy` [3338]; `embed/gene_vectors.npy` [3338]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3338 or target_col == 3338). Every well: [[KHDRBS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KHDRBS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
