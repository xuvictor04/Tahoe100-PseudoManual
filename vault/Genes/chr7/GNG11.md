---
symbol: "GNG11"
type: "gene"
col: 4841
ensembl_id: "ENSG00000127920"
name: "G protein subunit gamma 11"
location: "7q21.3"
module: 19
arm: "+"
pooled_cpm: 16.2
n_lines_expressing: 29
n_dd_up: 10
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 12
direction_downstream: 15
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# GNG11

*G protein subunit gamma 11* — 7q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.63× (z +13.0, q 9e-36, up in 22 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Vilanterol (drug)]] 5 µM: 1.44× (z +3.5, q 0.035, up in 18 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.820× (z -4.6, q 0.002, down in 13 of 27 measured lines) ⚠ position not correctable. The strongest without an alert is [[Trametinib (drug)]] 5 µM: 0.511× (z -4.3, q 0.005, down in 19 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H460 0.242×, NCI-H1792 0.186×, RPMI-7951 0.269×); [[Trametinib (drug)]] 5 µM in 2 lines (NCI-H460 0.165×, NCI-H23 0.142×); [[Panobinostat (drug)]] 5 µM in 2 lines (HS-578T 0.141×, NCI-H460 0.193×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERPIND1]] (+0.70, fdr 7e-06), [[FST]] (+0.64, fdr 1e-05), [[TFPI2]] (+0.61, fdr 1e-05, ⚠ same locus), [[STEAP1B-AS1]] (+0.60, fdr 9e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[BMPER]] → it (grade B ⚠); 15 go from it, the strongest it → [[BEX3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4841.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.63×** | +13.0 | 9e-36 | 22/23 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.04×** | +10.7 | 4e-24 | 18/18 (C32, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.77×** | +8.4 | 7e-15 | 19/20 (RPMI-7951, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **2.08×** | +5.0 | 7e-05 | 15/24 (A-172, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +4.9 | 9e-05 | 14/24 (NCI-H2030, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.68×** | +3.6 | 0.033 | 10/26 (A-172, A498, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.035 | 18/27 (RPMI-7951, H4, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +3.3 | 0.071 | 4/26 (C32, A-172, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.071 | 8/25 (J82, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.1 | 0.094 | 11/26 (A498, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4841.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H460 0.242×, NCI-H1792 0.186×, RPMI-7951 0.269×); [[Trametinib (drug)]] 5 µM in 2 lines (NCI-H460 0.165×, NCI-H23 0.142×); [[Panobinostat (drug)]] 5 µM in 2 lines (HS-578T 0.141×, NCI-H460 0.193×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.820×** | -4.6 | 0.002 | 13/27 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.511×** | -4.3 | 0.005 | 19/27 (NCI-H460, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | 0.610× | -3.4 | 0.13 | 16/27 (NCI-H460, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.599× | -3.3 | 0.13 | 12/27 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.623× | -3.3 | 0.13 | 12/27 (H4, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.636× | -3.1 | 0.18 | 15/27 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4841. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 59.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 32.6 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.70× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 55.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.86× (z +9.2) ⚠ toxic; transcription drop | [[Trametinib (drug)]] 5 µM 0.142× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 81.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.37× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -9.7) |
| [[A498 (line)]] | wt | 30.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.64× (z +10.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 12.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.21× (z +9.9) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 18.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.5× (z +10.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 61.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.85× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 65.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.141× (z -9.5) |
| [[PANC-1 (line)]] | alt | 6.18 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.07× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.02 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.05 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4841), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPIND1]] | +0.70 | +0.71 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[FST]] | +0.64 | +0.65 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[TFPI2]] | +0.61 | +0.55 / +0.70 | both halves | 1e-05 | ⚠ same locus (31.0 kb: neighbours can correlate without regulation) |
| [[STEAP1B-AS1]] | +0.60 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[SGIP1]] | +0.59 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[GJA1]] | +0.59 | +0.68 / +0.52 | both halves | 1e-05 | pathway: Cellular responses to mechanical stimuli |
| [[GRAMD1B]] | +0.58 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[CRLF2]] | +0.58 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[ESM1]] | +0.55 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[ANGPTL2]] | +0.55 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[SERPINE2]] | +0.55 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[TMEM158]] | +0.54 | +0.55 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[DOCK4]] | +0.54 | +0.56 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 2, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMPER]] | B | BMPER activity raises GNG11's level | lines that do not express BMPER (21) vs lines expressing it (29) | 3.68× lower at baseline in the lines without BMPER | 0.014 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[MMP1]] | B | MMP1 activity raises GNG11's level | lines that do not express MMP1 (26) vs lines expressing it (24) | 3.24× lower at baseline in the lines without MMP1 | 0.098 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |
| [[GJA1]] | C | GJA1 activity raises GNG11's level | lines that do not express GJA1 (26) vs lines expressing it (24) | 5.41× lower at baseline in the lines without GJA1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1; co-absent with the target |
| [[SPOCK1]] | C | SPOCK1 activity raises GNG11's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 5.04× lower at baseline in the lines without SPOCK1 | 0.015 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41; co-absent with the target |
| [[PDE7B]] | C | PDE7B activity raises GNG11's level | lines that do not express PDE7B (26) vs lines expressing it (24) | 3.04× lower at baseline in the lines without PDE7B | 0.024 | ⚠ within organs, on part of the lines; also absent: ZMAT4, ANGPTL2, LUM; maybe low, not absent; co-absent with the target |
| [[IL6]] | C | IL6 activity raises GNG11's level | lines that do not express IL6 (32) vs lines expressing it (18) | 4.25× lower at baseline in the lines without IL6 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2; co-absent with the target |
| [[CDH11]] | C | CDH11 activity raises GNG11's level | lines that do not express CDH11 (36) vs lines expressing it (14) | 3.95× lower at baseline in the lines without CDH11 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX11, ENSG00000253693, ENSG00000238054; co-absent with the target |
| [[IL13RA2]] | C | IL13RA2 activity raises GNG11's level | lines that do not express IL13RA2 (36) vs lines expressing it (14) | 3.40× lower at baseline in the lines without IL13RA2 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286523, LINC02476, PAX3; co-absent with the target |
| [[ADAMTS6]] | C | ADAMTS6 activity raises GNG11's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 3.19× lower at baseline in the lines without ADAMTS6 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2; co-absent with the target |
| [[LINC02454]] | C | LINC02454 activity raises GNG11's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 3.81× lower at baseline in the lines without LINC02454 | 0.068 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent; co-absent with the target |
| [[IGFBP7]] | C | IGFBP7 activity raises GNG11's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 3.83× lower at baseline in the lines without IGFBP7 | 0.089 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1; co-absent with the target |
| [[COL4A6]] | C | COL4A6 activity raises GNG11's level | lines that do not express COL4A6 (36) vs lines expressing it (14) | 2.93× lower at baseline in the lines without COL4A6 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX7, ENSG00000238054, LINC01035; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 6, C 9. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BEX3]] | B | GNG11 activity raises BEX3's level | lines that do not express GNG11 (21) vs lines expressing it (29) | 2.37× lower at baseline in the lines without GNG11 | 0.062 | ⚠ within organs, on part of the lines; also absent: LOXL2, SLC8A1, NALCN |
| cells under [[Bortezomib (drug)]] 0.05 µM | B | GNG11 activity lowers the cells' numbers under Bortezomib 0.05 µM (makes them more sensitive) | lines that do not express GNG11 (21) vs lines expressing it (27) | the lines without GNG11: 1.34× the cells of the other lines | 0.066 | ⚠ within organs, on part of the lines; also absent: LOXL2, SLC8A1, NALCN |
| [[AP1S2]] | B | GNG11 activity raises AP1S2's level | lines that do not express GNG11 (21) vs lines expressing it (29) | 1.79× lower at baseline in the lines without GNG11 | 0.076 | ⚠ within organs, on part of the lines; also absent: LOXL2, SLC8A1, NALCN |
| [[PRDM8]] | B | GNG11 activity lowers PRDM8's level | lines that do not express GNG11 (21) vs lines expressing it (29) | 1.09× higher at baseline in the lines without GNG11 | 0.089 | ⚠ within organs, on part of the lines; also absent: LOXL2, SLC8A1, NALCN |
| cells under [[5-Azacytidine (drug)]] 5 µM | B | GNG11 activity lowers the cells' numbers under 5-Azacytidine 5 µM (makes them more sensitive) | lines that do not express GNG11 (21) vs lines expressing it (27) | the lines without GNG11: 1.27× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: LOXL2, SLC8A1, NALCN |
| [[ETV1]] | B | GNG11 activity raises ETV1's level | lines that do not express GNG11 (21) vs lines expressing it (29) | 2.95× lower at baseline in the lines without GNG11 | 0.094 | ⚠ within organs, on part of the lines; also absent: LOXL2, SLC8A1, NALCN |
| [[IGFBP7]] | C | GNG11 activity raises IGFBP7's level | lines that do not express GNG11 (21) vs lines expressing it (29) | 7.07× lower at baseline in the lines without GNG11 | 0.003 | ⚠ within organs, on part of the lines; also absent: LOXL2, SLC8A1, NALCN; co-absent with the target |
| [[GJA1]] | C | GNG11 activity raises GJA1's level | lines that do not express GNG11 (21) vs lines expressing it (29) | 5.58× lower at baseline in the lines without GNG11 | 0.011 | ⚠ within organs, on part of the lines; also absent: LOXL2, SLC8A1, NALCN; co-absent with the target |
| [[SLC16A6]] | C | GNG11 activity raises SLC16A6's level | lines that do not express GNG11 (21) vs lines expressing it (29) | 2.73× lower at baseline in the lines without GNG11 | 0.012 | ⚠ within organs, on part of the lines; also absent: LOXL2, SLC8A1, NALCN; co-absent with the target |
| [[IL6]] | C | GNG11 activity raises IL6's level | lines that do not express GNG11 (21) vs lines expressing it (29) | 6.69× lower at baseline in the lines without GNG11 | 0.041 | ⚠ within organs, on part of the lines; also absent: LOXL2, SLC8A1, NALCN; co-absent with the target |
| [[STEAP1B-AS1]] | C | GNG11 activity raises STEAP1B-AS1's level | lines that do not express GNG11 (21) vs lines expressing it (29) | 2.90× lower at baseline in the lines without GNG11 | 0.048 | ⚠ within organs, on part of the lines; also absent: LOXL2, SLC8A1, NALCN; co-absent with the target |
| [[CDH13]] | C | GNG11 activity raises CDH13's level | lines that do not express GNG11 (21) vs lines expressing it (29) | 3.97× lower at baseline in the lines without GNG11 | 0.066 | ⚠ within organs, on part of the lines; also absent: LOXL2, SLC8A1, NALCN; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.472). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.7, 15.9); signed map (19.5, 52.7). **Vector** length 71.6, 22.6% of its response variance represented; |z| ≥ 3 in 515 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +13.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +10.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +1.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +1.5 |
|  | [[Vitamin K4 (drug)]] 0.05 µM |  | +1.4 | +1.6 |
|  | [[Benztropine (mesylate) (drug)]] 0.05 µM |  | +1.3 | +1.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.2 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.1 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit gamma 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.3 — chr7:93,921,735-93,928,610 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GNGT11 |
| Gene groups (HGNC) | G protein subunits gamma |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 66 pathways, smallest: G beta:gamma signalling through BTK; Prostacyclin signalling through prostacyclin receptor; G beta:gamma signalling through PLC beta |
| Matched by | ensembl_id |

**Function**, from UniProt [P61952](https://www.uniprot.org/uniprotkb/P61952) (Guanine nucleotide-binding protein G(I)/G(S)/G(O) subunit gamma-11):

> Guanine nucleotide-binding proteins (G proteins) are involved as a modulator or transducer in various transmembrane signaling systems. The beta and gamma chains are required for the GTPase activity, for replacement of GDP by GTP, and for G protein-effector interaction.

**Summary**, from NCBI Gene [2791](https://www.ncbi.nlm.nih.gov/gene/2791):

> This gene is a member of the guanine nucleotide-binding protein (G protein) gamma family and encodes a lipid-anchored, cell membrane protein. As a member of the heterotrimeric G protein complex, this protein plays a role in this transmembrane signaling system. This protein is also subject to carboxyl-terminal processing. Decreased expression of this gene is associated with splenic marginal zone lymphomas. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4403](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4403) · Entrez [2791](https://www.ncbi.nlm.nih.gov/gene/2791) · UniProt [P61952](https://www.uniprot.org/uniprotkb/P61952) · Ensembl [ENSG00000127920](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127920)

## Data

Gene col 4841: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4841); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4841, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4841]; `tensor/DDL_lfc|DDL_z.npy` [4841]; `embed/gene_vectors.npy` [4841]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4841 or target_col == 4841). Every well: [[GNG11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNG11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
