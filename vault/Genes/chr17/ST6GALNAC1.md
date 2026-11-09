---
symbol: "ST6GALNAC1"
type: "gene"
col: 955
ensembl_id: "ENSG00000070526"
name: "ST6 N-acetylgalactosaminide alpha-2,6-sialyltransferase 1"
location: "17q25.1"
module: 44
arm: "+"
pooled_cpm: 2.29
n_lines_expressing: 13
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 49
direction_downstream: 126
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# ST6GALNAC1

*ST6 N-acetylgalactosaminide alpha-2,6-sialyltransferase 1* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.12× (z +10.4, q 8e-23, up in 3 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.72× (z +10.2, q 3e-22, up in 1 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Artesunate (drug)]] 0.5 µM: 0.453× (z -4.4, q 0.006, down in 2 of 10 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (KATO III 0.0709×, LS 180 0.0793×; ⚠ cell-cycle shift, explains ~36% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (KATO III 0.0647×, LS 180 0.1000×); [[Panobinostat (drug)]] 5 µM in 2 lines (KATO III 0.0790×, LS 180 0.0797×; ⚠ cell-cycle shift, explains ~21% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (KATO III 0.173×, COLO 205 0.0550×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (KATO III 0.196×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R1B]] (+0.87, fdr 7e-06), [[MUC5B]] (+0.86, fdr 7e-06), [[C9orf152]] (+0.83, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 49 arrows point to it, the strongest [[NAA11]] → it (grade C ⚠); 126 go from it, the strongest it → [[PROM2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 955.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.12×** | +10.4 | 8e-23 | 3/3 (CFPAC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.58×** | +10.4 | 8e-23 | 4/4 (CFPAC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.72×** | +10.2 | 3e-22 | 1/9 (NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.73×** | +8.6 | 2e-15 | 3/3 (CFPAC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.84×** | +5.7 | 1e-06 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.78×** | +5.6 | 2e-06 | 0/9 | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.82×** | +5.5 | 3e-06 | 1/4 (CFPAC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.63×** | +5.1 | 3e-05 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.30×** | +4.6 | 3e-04 | 0/6 | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.27×** | +4.5 | 4e-04 | 0/5 | top dose only | cell-cycle shift (explains ~9% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.07×** | +4.0 | 0.003 | 1/1 (CFPAC-1) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +4.0 | 0.003 | 1/6 (CFPAC-1) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Tazarotene (drug)]] 0.5 µM |  | **1.97×** | +3.7 | 0.008 | 1/10 (LoVo) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.92×** | +3.6 | 0.014 | 3/4 (COLO 205, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.30×** | +3.3 | 0.043 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +3.2 | 0.045 | 0/11 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 955.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (KATO III 0.0709×, LS 180 0.0793×; ⚠ cell-cycle shift, explains ~36% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (KATO III 0.0647×, LS 180 0.1000×); [[Panobinostat (drug)]] 5 µM in 2 lines (KATO III 0.0790×, LS 180 0.0797×; ⚠ cell-cycle shift, explains ~21% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (KATO III 0.173×, COLO 205 0.0550×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (KATO III 0.196×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | **0.453×** | -4.4 | 0.006 | 2/10 (HepG2/C3A, Panc 03.27) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | 0.314× | -3.4 | 0.16 | 2/10 (CFPAC-1, Panc 03.27) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | 0.551× | -3.3 | 0.16 | 0/10 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 955. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 36.1 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0709× (z -19.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0647× (z -14.2) |
| [[LS 180 (line)]] | wt | 34.6 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0793× (z -16.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.1000× (z -10.9) |
| [[COLO 205 (line)]] | alt | 7.38 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0550× (z -8.5) |
| [[A-172 (line)]] | wt | 0.249 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.224 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.258 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.225 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.355 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.335 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.257 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.270 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.294 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.365 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.623 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.278 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.819 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.229 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.878 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.332 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.206 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.681 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.251 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.184 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.717 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.206 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.264 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.953 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.228 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.240 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.211 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.303 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.212 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.235 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.316 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.279 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.284 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.248 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.246 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.245 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.243 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 955), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R1B]] | +0.87 | +0.81 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[MUC5B]] | +0.86 | +0.81 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[C9orf152]] | +0.83 | +0.78 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[TSPAN8]] | +0.81 | +0.82 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[UGT1A1]] | +0.81 | +0.77 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[GPA33]] | +0.79 | +0.72 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[GPX2]] | +0.79 | +0.77 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[PRR15L]] | +0.79 | +0.77 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[CFTR]] | +0.78 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[LGALS4]] | +0.77 | +0.79 / +0.69 | both halves | 7e-06 |  |
| [[LINC01819]] | +0.77 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[NPSR1]] | +0.76 | +0.79 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*49 arrows, 49 of them with an alert ⚠; grade A 0, B 0, C 49. Shown: the 12 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NAA11]] | C | NAA11 activity raises ST6GALNAC1's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 1.61× lower at baseline in the lines without NAA11 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent; co-absent with the target |
| [[PIGR]] | C | PIGR activity raises ST6GALNAC1's level | lines that do not express PIGR (45) vs lines expressing it (5) | 3.44× lower at baseline in the lines without PIGR | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target |
| [[AGR3]] | C | AGR3 activity raises ST6GALNAC1's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 4.51× lower at baseline in the lines without AGR3 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[TCN1]] | C | TCN1 activity raises ST6GALNAC1's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 2.79× lower at baseline in the lines without TCN1 | 0.005 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B; co-absent with the target |
| [[MUC5B]] | C | MUC5B activity raises ST6GALNAC1's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 2.82× lower at baseline in the lines without MUC5B | 0.009 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925; co-absent with the target |
| [[SLC44A4]] | C | SLC44A4 activity raises ST6GALNAC1's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 2.97× lower at baseline in the lines without SLC44A4 | 0.011 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; co-absent with the target |
| [[MUC6]] | C | MUC6 activity raises ST6GALNAC1's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 2.08× lower at baseline in the lines without MUC6 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |
| [[LINC02474]] | C | LINC02474 activity raises ST6GALNAC1's level | lines that do not express LINC02474 (40) vs lines expressing it (10) | 3.02× lower at baseline in the lines without LINC02474 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC4, SFTPA2, ENSG00000230975; co-absent with the target |
| [[SLC6A14]] | C | SLC6A14 activity raises ST6GALNAC1's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 2.91× lower at baseline in the lines without SLC6A14 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1; co-absent with the target |
| [[PLA2G2A]] | C | PLA2G2A activity raises ST6GALNAC1's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 3.06× lower at baseline in the lines without PLA2G2A | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1; co-absent with the target |
| [[MUC5AC]] | C | MUC5AC activity raises ST6GALNAC1's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 2.78× lower at baseline in the lines without MUC5AC | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3; co-absent with the target |
| [[RNF183]] | C | RNF183 activity raises ST6GALNAC1's level | lines that do not express RNF183 (36) vs lines expressing it (14) | 2.47× lower at baseline in the lines without RNF183 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, LINC02964, VIL1; co-absent with the target |

### Downstream of this gene

*126 arrows, 126 of them with an alert ⚠; grade A 0, B 26, C 100. Shown: the 12 strongest; 114 more arrows (114 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PROM2]] | B | ST6GALNAC1 activity raises PROM2's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 2.97× lower at baseline in the lines without ST6GALNAC1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4 |
| [[MANSC1]] | B | ST6GALNAC1 activity raises MANSC1's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 3.04× lower at baseline in the lines without ST6GALNAC1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4 |
| [[ARHGEF16]] | B | ST6GALNAC1 activity raises ARHGEF16's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 3.08× lower at baseline in the lines without ST6GALNAC1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4 |
| [[SLC12A2]] | B | ST6GALNAC1 activity raises SLC12A2's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 2.69× lower at baseline in the lines without ST6GALNAC1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4 |
| [[MGST2]] | B | ST6GALNAC1 activity raises MGST2's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 3.35× lower at baseline in the lines without ST6GALNAC1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4 |
| [[FUT2]] | B | ST6GALNAC1 activity raises FUT2's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 2.39× lower at baseline in the lines without ST6GALNAC1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4 |
| [[FAAH]] | B | ST6GALNAC1 activity raises FAAH's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 1.66× lower at baseline in the lines without ST6GALNAC1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4 |
| [[LINC02580]] | B | ST6GALNAC1 activity raises LINC02580's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 2.02× lower at baseline in the lines without ST6GALNAC1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4 |
| [[UGT8]] | B | ST6GALNAC1 activity raises UGT8's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 3.35× lower at baseline in the lines without ST6GALNAC1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4 |
| [[MROH7]] | B | ST6GALNAC1 activity raises MROH7's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 1.96× lower at baseline in the lines without ST6GALNAC1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4 |
| [[PLCH1]] | B | ST6GALNAC1 activity raises PLCH1's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 2.53× lower at baseline in the lines without ST6GALNAC1 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4 |
| cells under [[Afatinib (drug)]] 0.5 µM | B | ST6GALNAC1 activity lowers the cells' numbers under Afatinib 0.5 µM (makes them more sensitive) | lines that do not express ST6GALNAC1 (37) vs lines expressing it (11) | the lines without ST6GALNAC1: 1.13× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.854). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.1, 50.8); signed map (64.0, 5.8). **Vector** length 33.6, 11.5% of its response variance represented; |z| ≥ 3 in 236 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.64 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.64 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.64 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +10.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +5.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.7 | +3.3 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -0.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -4.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -1.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ST6 N-acetylgalactosaminide alpha-2,6-sialyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:76,624,761-76,643,786 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ST6GalNAcI; previously SIAT7A |
| Gene groups (HGNC) | Sialyltransferases |
| Reactome | 4 pathways, smallest: Sialic acid metabolism; Synthesis of substrates in N-glycan biosythesis; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NSC7](https://www.uniprot.org/uniprotkb/Q9NSC7) (Alpha-N-acetylgalactosaminide alpha-2,6-sialyltransferase 1):

> Protein sialyltransferase specifically expressed in goblet cells that plays a key role in intestinal host-commensal homeostasis. Conjugates sialic acid with an alpha-2-6 linkage to N-acetylgalactosamine (GalNAc) glycan chains linked to serine or threonine in glycoproteins. Catalyzes the formation of the sialyl-Tn (S-Tn) antigen, an antigen found in intestinal goblet cells, as well as ulcerative colitis (UC) and various cancers. Protein sialylation in globlet cells is essential for mucus …

**Summary**, from NCBI Gene [55808](https://www.ncbi.nlm.nih.gov/gene/55808):

> Glycosylation of proteins affects cell-cell interaction, interactions with the matrix, and the functions of intracellular molecules. ST6GALNAC1 transfers a sialic acid, N-acetylneuraminic acid (NeuAc), in an alpha-2,6 linkage to O-linked GalNAc residues. The cancer-associated sialyl-Tn (sTn) antigen is formed by ST6GALNAC1-catalyzed sialylation of GalNAc residues on mucins (Ikehara et al., 1999 [PubMed 10536037]; Sewell et al., 2006 [PubMed 16319059]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:23614](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23614) · Entrez [55808](https://www.ncbi.nlm.nih.gov/gene/55808) · UniProt [Q9NSC7](https://www.uniprot.org/uniprotkb/Q9NSC7) · Ensembl [ENSG00000070526](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070526)

## Data

Gene col 955: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 955); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 955, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 955]; `tensor/DDL_lfc|DDL_z.npy` [955]; `embed/gene_vectors.npy` [955]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 955 or target_col == 955). Every well: [[ST6GALNAC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ST6GALNAC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
