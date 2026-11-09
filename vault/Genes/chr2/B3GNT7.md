---
symbol: "B3GNT7"
type: "gene"
col: 8028
ensembl_id: "ENSG00000156966"
name: "UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 7"
location: "2q37.1"
module: 8
arm: "+"
pooled_cpm: 2.94
n_lines_expressing: 19
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 22
direction_downstream: 29
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# B3GNT7

*UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 7* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.34× (z +13.2, q 8e-37, up in 1 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 2.32× (z +4.2, q 0.002, up in 0 of 8 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.550× (z -4.3, q 0.009, down in 11 of 16 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LGALS9]] (+0.59, fdr 2e-05), [[CEACAM1]] (+0.56, fdr 2e-05), [[ST6GALNAC2]] (+0.54, fdr 2e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[ATAD3C]] → it (grade B ⚠); 29 go from it, the strongest it → [[TMEM51-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8028.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.34×** | +13.2 | 8e-37 | 1/4 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.66×** | +9.1 | 3e-17 | 1/9 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.27×** | +7.7 | 3e-12 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.12×** | +5.2 | 2e-05 | 4/9 (PANC-1, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.81×** | +5.2 | 3e-05 | 0/7 | two highest doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +4.9 | 8e-05 | 2/12 (C32, SW480) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +4.2 | 0.002 | 2/11 (SW1417, C32) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.32×** | +4.2 | 0.002 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +4.1 | 0.003 | 1/13 (A549) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +3.4 | 0.032 | 0/9 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.63×** | +3.4 | 0.036 | 1/13 (A549) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.67×** | +3.3 | 0.046 | 1/10 (SW480) | inconsistent across doses | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.067 | 3/17 (CFPAC-1, PANC-1, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.35×** | +3.1 | 0.088 | 0/6 | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8028.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.550×** | -4.3 | 0.009 | 11/16 (A549, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.558×** | -4.2 | 0.009 | 10/17 (PANC-1, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.583×** | -3.9 | 0.022 | 1/17 (PANC-1) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.619×** | -3.4 | 0.083 | 7/17 (C32, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8028. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 16.3 | 0 | 9 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0592× (z -15.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.189× (z -8.9) |
| [[KATO III (line)]] | alt | 16.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0754× (z -17.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0716× (z -12.3) |
| [[C32 (line)]] | wt | 6.75 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0435× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 7.59 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0514× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 6.54 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 0.781 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0948× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.257 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.411 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.257 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.313 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.404 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.245 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.285 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.270 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.130 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.227 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.412 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.173 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.636 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.169 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.159 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.190 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.298 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.702 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.204 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.586 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8028), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LGALS9]] | +0.59 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[CEACAM1]] | +0.56 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[ST6GALNAC2]] | +0.54 | +0.56 / +0.47 | both halves | 2e-05 | pathway: O-linked glycosylation |
| [[MUC16]] | +0.54 | +0.45 / +0.55 | both halves | 3e-05 | pathway: O-linked glycosylation; STRING 403 |
| [[ALOX5]] | +0.52 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[CDH3]] | +0.52 | +0.37 / +0.47 | both halves | 9e-05 |  |
| [[MUC4]] | +0.52 | +0.49 / +0.53 | both halves | 1e-05 | pathway: O-linked glycosylation; STRING 497 |
| [[GABRP]] | +0.51 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[PCDH1]] | +0.49 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[VILL]] | +0.49 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[P2RY2]] | +0.49 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[LOXL4]] | +0.48 | +0.41 / +0.45 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 5, C 17. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATAD3C]] | B | ATAD3C activity raises B3GNT7's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 1.84× lower at baseline in the lines without ATAD3C | 0.039 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |
| [[TMEM51-AS1]] | B | TMEM51-AS1 activity raises B3GNT7's level | lines that do not express TMEM51-AS1 (13) vs lines expressing it (37) | 1.62× lower at baseline in the lines without TMEM51-AS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: RAB17, PLEKHG1, EPHA1; maybe low, not absent |
| [[CRACR2B]] | B | CRACR2B activity raises B3GNT7's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 1.75× lower at baseline in the lines without CRACR2B | 0.081 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[JUP]] | B | JUP activity raises B3GNT7's level | lines that do not express JUP (16) vs lines expressing it (34) | 1.57× lower at baseline in the lines without JUP | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[ST6GALNAC2]] | B | ST6GALNAC2 activity raises B3GNT7's level | lines that do not express ST6GALNAC2 (8) vs lines expressing it (42) | 1.85× lower at baseline in the lines without ST6GALNAC2 | 0.088 | ⚠ within organs, on part of the lines; also absent: CELSR1, CTSD, TRIM47; maybe low, not absent |
| [[LY75]] | C | LY75 activity raises B3GNT7's level | lines that do not express LY75 (30) vs lines expressing it (20) | 2.13× lower at baseline in the lines without LY75 | 0.006 | ⚠ within organs, on part of the lines; also absent: IL20RA, TINAGL1, CARD11; co-absent with the target |
| [[SHROOM4]] | C | SHROOM4 activity raises B3GNT7's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 1.69× lower at baseline in the lines without SHROOM4 | 0.013 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539; co-absent with the target |
| [[GPRIN2]] | C | GPRIN2 activity raises B3GNT7's level | lines that do not express GPRIN2 (31) vs lines expressing it (19) | 1.87× lower at baseline in the lines without GPRIN2 | 0.017 | ⚠ within organs, on part of the lines; also absent: MUC16, KRT6A, ACP7; co-absent with the target |
| [[MUC16]] | C | MUC16 activity raises B3GNT7's level | lines that do not express MUC16 (38) vs lines expressing it (12) | 2.28× lower at baseline in the lines without MUC16 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSDMC, S100A9, STEAP4; co-absent with the target |
| [[CEACAM1]] | C | CEACAM1 activity raises B3GNT7's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 2.11× lower at baseline in the lines without CEACAM1 | 0.033 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29; co-absent with the target |
| [[HES2]] | C | HES2 activity raises B3GNT7's level | lines that do not express HES2 (20) vs lines expressing it (30) | 1.80× lower at baseline in the lines without HES2 | 0.052 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2; co-absent with the target |
| [[RAB25]] | C | RAB25 activity raises B3GNT7's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 1.78× lower at baseline in the lines without RAB25 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |

### Downstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 10, C 19. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM51-AS1]] | B | B3GNT7 activity raises TMEM51-AS1's level | lines that do not express B3GNT7 (31) vs lines expressing it (19) | 2.45× lower at baseline in the lines without B3GNT7 | 0.013 | ⚠ within organs, on part of the lines; also absent: KRT23, PROM1, HSD17B2 |
| [[TSPAN14]] | B | B3GNT7 activity raises TSPAN14's level | lines that do not express B3GNT7 (31) vs lines expressing it (19) | 1.62× lower at baseline in the lines without B3GNT7 | 0.037 | ⚠ within organs, on part of the lines; also absent: KRT23, PROM1, HSD17B2 |
| [[DAB2IP]] | B | B3GNT7 activity raises DAB2IP's level | lines that do not express B3GNT7 (31) vs lines expressing it (19) | 1.69× lower at baseline in the lines without B3GNT7 | 0.043 | ⚠ within organs, on part of the lines; also absent: KRT23, PROM1, HSD17B2 |
| [[ST6GALNAC2]] | B | B3GNT7 activity raises ST6GALNAC2's level | lines that do not express B3GNT7 (31) vs lines expressing it (19) | 1.84× lower at baseline in the lines without B3GNT7 | 0.060 | ⚠ within organs, on part of the lines; also absent: KRT23, PROM1, HSD17B2 |
| [[SEMA4D]] | B | B3GNT7 activity raises SEMA4D's level | lines that do not express B3GNT7 (31) vs lines expressing it (19) | 1.25× lower at baseline in the lines without B3GNT7 | 0.071 | ⚠ within organs, on part of the lines; also absent: KRT23, PROM1, HSD17B2 |
| [[TRPV4]] | B | B3GNT7 activity raises TRPV4's level | lines that do not express B3GNT7 (31) vs lines expressing it (19) | 2.12× lower at baseline in the lines without B3GNT7 | 0.074 | ⚠ within organs, on part of the lines; also absent: KRT23, PROM1, HSD17B2 |
| [[CORO2A]] | B | B3GNT7 activity raises CORO2A's level | lines that do not express B3GNT7 (31) vs lines expressing it (19) | 1.60× lower at baseline in the lines without B3GNT7 | 0.079 | ⚠ within organs, on part of the lines; also absent: KRT23, PROM1, HSD17B2 |
| [[VILL]] | B | B3GNT7 activity strengthens VILL's drug response | lines that do not express B3GNT7 (16) vs lines expressing it (14) | the lines without B3GNT7 respond 0.45× as strongly (z diff +1.53); strongest at Harringtonine 5 µM: 0.64x vs 0.34x (z diff +2.4) | 0.081 | ⚠ within organs, on part of the lines; also absent: KRT23, PROM1, HSD17B2; target measured in part of the lines; artifact flags |
| [[PLEKHS1]] | B | B3GNT7 activity raises PLEKHS1's level | lines that do not express B3GNT7 (31) vs lines expressing it (19) | 1.70× lower at baseline in the lines without B3GNT7 | 0.081 | ⚠ within organs, on part of the lines; also absent: KRT23, PROM1, HSD17B2 |
| [[LGALS9]] | B | B3GNT7 activity raises LGALS9's level | lines that do not express B3GNT7 (31) vs lines expressing it (19) | 2.02× lower at baseline in the lines without B3GNT7 | 0.096 | ⚠ within organs, on part of the lines; also absent: KRT23, PROM1, HSD17B2 |
| [[KRT23]] | C | B3GNT7 activity raises KRT23's level | lines that do not express B3GNT7 (31) vs lines expressing it (19) | 3.50× lower at baseline in the lines without B3GNT7 | 0.009 | ⚠ within organs, on part of the lines; also absent: KRT23, PROM1, HSD17B2; co-absent with the target |
| [[HES2]] | C | B3GNT7 activity raises HES2's level | lines that do not express B3GNT7 (31) vs lines expressing it (19) | 1.97× lower at baseline in the lines without B3GNT7 | 0.009 | ⚠ within organs, on part of the lines; also absent: KRT23, PROM1, HSD17B2; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.422). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.7, 53.6); signed map (59.1, 10.5). **Vector** length 41.1, 10.3% of its response variance represented; |z| ≥ 3 in 430 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.8 | +9.1 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.6 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.0 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.8 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.8 | +1.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -1.6 | -1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -4.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -2.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.0 | -1.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -3.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -0.9 | -2.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -0.8 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:231,395,671-231,408,799 (+) |
| Ensembl biotype | protein_coding |
| Also known as | beta3GnT7 |
| Gene groups (HGNC) | Beta 3-glycosyltransferases |
| Reactome | 6 pathways, smallest: Keratan sulfate biosynthesis; Keratan sulfate/keratin metabolism; O-linked glycosylation of mucins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFL0](https://www.uniprot.org/uniprotkb/Q8NFL0) (UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 7):

> N-acetyl glucosamine (GlcNAc) transferase that catalyzes the transfer of GlcNAc via a beta1->3 linkage from UDP-GlcNAc to the non-reducing terminal galactose (Gal) in the linearly growing chain of N- and O-linked keratan sulfate proteoglycans. Cooperates with B4GALT4 galactosyltransferase and CHST6 and CHST1 sulfotransferases to construct and elongate mono- and disulfated disaccharide units [->3Galbeta1->4(6-sulfoGlcNAcbeta)1->] and [->3(6-sulfoGalbeta)1->4(6-sulfoGlcNAcbeta)1->] within keratan …

**Summary**, from NCBI Gene [93010](https://www.ncbi.nlm.nih.gov/gene/93010):

> Enables N-acetyllactosaminide beta-1,3-N-acetylglucosaminyltransferase activity. Involved in keratan sulfate proteoglycan biosynthetic process. Predicted to be located in membrane. Predicted to be active in Golgi membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18811](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18811) · Entrez [93010](https://www.ncbi.nlm.nih.gov/gene/93010) · UniProt [Q8NFL0](https://www.uniprot.org/uniprotkb/Q8NFL0) · Ensembl [ENSG00000156966](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156966)

## Data

Gene col 8028: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8028); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8028, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8028]; `tensor/DDL_lfc|DDL_z.npy` [8028]; `embed/gene_vectors.npy` [8028]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8028 or target_col == 8028). Every well: [[B3GNT7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B3GNT7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
