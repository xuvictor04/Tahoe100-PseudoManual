---
symbol: "CGA"
type: "gene"
col: 5688
ensembl_id: "ENSG00000135346"
name: "glycoprotein hormones, alpha polypeptide"
location: "6q14.3"
module: 9
arm: "+"
pooled_cpm: 5.41
n_lines_expressing: 6
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 23
direction_downstream: 46
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# CGA

*glycoprotein hormones, alpha polypeptide* — 6q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.91× (z +8.9, q 3e-16, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.18× (z +7.5, q 8e-12, up in 1 of 2 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.0380×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SHP-77 0.0472×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CALCA]] (+0.88, fdr 7e-06), [[SRRM4]] (+0.85, fdr 7e-06), [[RIT2]] (+0.83, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[CALCA]] → it (grade C ⚠); 46 go from it, the strongest it → [[RNF152]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5688.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.91×** | +8.9 | 3e-16 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.17×** | +8.7 | 7e-16 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.90×** | +7.6 | 8e-12 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.18×** | +7.5 | 8e-12 | 1/2 (NCI-H1573) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **4.25×** | +6.4 | 2e-08 | 0/1 | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.23×** | +5.2 | 2e-05 | 2/2 (SHP-77, NCI-H1573) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **4.06×** | +3.6 | 0.022 | 0/2 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.73×** | +3.6 | 0.026 | 0/3 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.14×** | +3.5 | 0.032 | 0/1 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.05×** | +3.4 | 0.044 | 0/1 | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.01×** | +3.2 | 0.072 | 0/2 | top dose only |  |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.99×** | +3.2 | 0.074 | 0/2 | rises with dose |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.62×** | +3.1 | 0.075 | 0/2 | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.97×** | +3.1 | 0.075 | 0/2 | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.94×** | +3.0 | 0.093 | 1/2 (NCI-H1573) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5688.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.0380×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SHP-77 0.0472×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.484× | -3.4 | 0.29 | 0/3 | inconsistent across doses | position effect removed |
| [[Anethole trithione (drug)]] 0.05 µM |  | 0.493× | -3.3 | 0.29 | 0/3 | inconsistent across doses | position effect removed |
| [[Relugolix (drug)]] 5 µM |  | 0.632× | -3.0 | 0.47 | 1/3 (SHP-77) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5688. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 269 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0380× (z -19.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0472× (z -13.1) |
| [[A-172 (line)]] | wt | 0.576 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.490 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.495 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.448 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.818 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.586 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.918 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.704 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.712 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.684 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.657 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.709 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.597 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.652 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.840 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.973 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.588 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.683 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.892 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.621 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.535 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.675 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.670 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.727 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.945 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.800 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.906 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.584 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5688), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALCA]] | +0.88 | +0.83 / +0.72 | both halves | 7e-06 | pathway: G alpha (s) signalling events; STRING 477 |
| [[SRRM4]] | +0.85 | +0.88 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[RIT2]] | +0.83 | +0.80 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[LRFN2]] | +0.83 | +0.80 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[SYT4]] | +0.81 | +0.80 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[ASCL1]] | +0.81 | +0.79 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[GRIK1]] | +0.76 | +0.71 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[PCSK1]] | +0.74 | +0.65 / +0.66 | both halves | 7e-06 | pathway: Peptide hormone biosynthesis |
| [[LINC02197]] | +0.73 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[NELL1]] | +0.69 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[KHDRBS2]] | +0.68 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[SNTG1]] | +0.66 | +0.62 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 0, C 23. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALCA]] | C | CALCA activity raises CGA's level | lines that do not express CALCA (45) vs lines expressing it (5) | 7.46× lower at baseline in the lines without CALCA | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises CGA's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 5.33× lower at baseline in the lines without RIT2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises CGA's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 5.45× lower at baseline in the lines without SYT4 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[KCNB2]] | C | KCNB2 activity raises CGA's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 4.27× lower at baseline in the lines without KCNB2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |
| [[ASCL1]] | C | ASCL1 activity raises CGA's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 3.22× lower at baseline in the lines without ASCL1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[H19]] | C | H19 activity raises CGA's level | lines that do not express H19 (38) vs lines expressing it (12) | 2.27× lower at baseline in the lines without H19 | 0.012 | ⚠ within organs, on part of the lines; also absent: CALCA, SYT4, CGA; co-absent with the target |
| [[GTSF1]] | C | GTSF1 activity raises CGA's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 2.84× lower at baseline in the lines without GTSF1 | 0.020 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |
| [[NAA11]] | C | NAA11 activity raises CGA's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 2.53× lower at baseline in the lines without NAA11 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent; co-absent with the target |
| [[SRRM4]] | C | SRRM4 activity raises CGA's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 3.17× lower at baseline in the lines without SRRM4 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent; co-absent with the target |
| [[HGF]] | C | HGF activity raises CGA's level | lines that do not express HGF (38) vs lines expressing it (12) | 2.44× lower at baseline in the lines without HGF | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA; co-absent with the target |
| [[AK4P3]] | C | AK4P3 activity raises CGA's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 2.07× lower at baseline in the lines without AK4P3 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF; co-absent with the target |
| [[LINC02492]] | C | LINC02492 activity raises CGA's level | lines that do not express LINC02492 (32) vs lines expressing it (18) | 1.80× lower at baseline in the lines without LINC02492 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000260289, ENSG00000254337, RHOJ; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 13, C 33. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF152]] | B | CGA activity raises RNF152's level | lines that do not express CGA (44) vs lines expressing it (6) | 2.95× lower at baseline in the lines without CGA | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2 |
| [[KCNMB2]] | B | CGA activity raises KCNMB2's level | lines that do not express CGA (44) vs lines expressing it (6) | 6.01× lower at baseline in the lines without CGA | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2 |
| [[LINC02306]] | B | CGA activity raises LINC02306's level | lines that do not express CGA (44) vs lines expressing it (6) | 4.39× lower at baseline in the lines without CGA | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2 |
| [[MYT1L]] | B | CGA activity raises MYT1L's level | lines that do not express CGA (44) vs lines expressing it (6) | 3.55× lower at baseline in the lines without CGA | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2 |
| [[AGBL1]] | B | CGA activity raises AGBL1's level | lines that do not express CGA (44) vs lines expressing it (6) | 2.76× lower at baseline in the lines without CGA | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2 |
| [[NELL1]] | B | CGA activity raises NELL1's level | lines that do not express CGA (44) vs lines expressing it (6) | 3.86× lower at baseline in the lines without CGA | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2 |
| [[UNC80]] | B | CGA activity raises UNC80's level | lines that do not express CGA (44) vs lines expressing it (6) | 2.75× lower at baseline in the lines without CGA | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2 |
| [[RALYL]] | B | CGA activity raises RALYL's level | lines that do not express CGA (44) vs lines expressing it (6) | 3.17× lower at baseline in the lines without CGA | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2 |
| [[DGKB]] | B | CGA activity raises DGKB's level | lines that do not express CGA (44) vs lines expressing it (6) | 3.37× lower at baseline in the lines without CGA | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2 |
| [[VENTXP1]] | B | CGA activity raises VENTXP1's level | lines that do not express CGA (44) vs lines expressing it (6) | 3.25× lower at baseline in the lines without CGA | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2 |
| [[CHRM5]] | B | CGA activity raises CHRM5's level | lines that do not express CGA (44) vs lines expressing it (6) | 2.44× lower at baseline in the lines without CGA | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2 |
| [[GLRA3]] | B | CGA activity raises GLRA3's level | lines that do not express CGA (44) vs lines expressing it (6) | 2.54× lower at baseline in the lines without CGA | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2 |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.597). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.8, 37.0); signed map (44.7, 34.3). **Vector** length 9.37, 4.56% of its response variance represented; |z| ≥ 3 in 48 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +0.9 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.8 | +8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +0.8 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.7 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.7 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.4 | +1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.4 | -0.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.3 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.3 | +3.6 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.3 | -0.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.3 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.3 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.3 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.3 | -0.8 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.2 | -1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.2 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | glycoprotein hormones, alpha polypeptide |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.3 — chr6:87,085,498-87,095,106 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HCG, GPHa, GPHA1, FSHA, LHA, TSHA, GPA1 |
| Gene groups (HGNC) | Receptor ligands; Glycoprotein hormone subunits |
| Reactome | 21 pathways, smallest: Glycoprotein hormones; Androgen biosynthesis; Metabolism of amine-derived hormones |
| Matched by | ensembl_id |

**Function**, from UniProt [P01215](https://www.uniprot.org/uniprotkb/P01215) (Glycoprotein hormones alpha chain):

> Shared alpha chain of the active heterodimeric glycoprotein hormones thyrotropin/thyroid stimulating hormone/TSH, lutropin/luteinizing hormone/LH, follitropin/follicle stimulating hormone/FSH and choriogonadotropin/CG. These hormones bind specific receptors on target cells that in turn activate downstream signaling pathways.

**Summary**, from NCBI Gene [1081](https://www.ncbi.nlm.nih.gov/gene/1081):

> The four human glycoprotein hormones chorionic gonadotropin (CG), luteinizing hormone (LH), follicle stimulating hormone (FSH), and thyroid stimulating hormone (TSH) are dimers consisting of alpha and beta subunits that are associated noncovalently. The alpha subunits of these hormones are identical, however, their beta chains are unique and confer biological specificity. The protein encoded by this gene is the alpha subunit and belongs to the glycoprotein hormones alpha chain family. Two …

**Accessions** — [HGNC:1885](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1885) · Entrez [1081](https://www.ncbi.nlm.nih.gov/gene/1081) · UniProt [P01215](https://www.uniprot.org/uniprotkb/P01215) · Ensembl [ENSG00000135346](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135346)

## Data

Gene col 5688: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5688); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5688, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5688]; `tensor/DDL_lfc|DDL_z.npy` [5688]; `embed/gene_vectors.npy` [5688]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5688 or target_col == 5688). Every well: [[CGA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CGA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
