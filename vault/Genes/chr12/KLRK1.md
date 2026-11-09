---
symbol: "KLRK1"
type: "gene"
col: 13139
ensembl_id: "ENSG00000213809"
name: "killer cell lectin like receptor K1"
location: "12p13.2"
module: 223
arm: "+"
pooled_cpm: 3.32
n_lines_expressing: 21
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 22
tags: ["gene", "module/223"]
generated_by: "tahoemap"
---

# KLRK1

*killer cell lectin like receptor K1* — 12p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.36× (z +17.5, q 0e+00, up in 12 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.539× (z -4.6, q 0.002, down in 12 of 19 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Daptomycin (drug)]] 0.5 µM in 1 line (NCI-H23 0.114×; ⚠ unreliable plate only); [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 0.0988×); [[Bortezomib (drug)]] 0.05 µM in 1 line (SW 900 0.0778×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLRC4-KLRK1]] (+0.95, fdr 7e-06, ⚠ same locus), [[KLRC3]] (+0.90, fdr 7e-06, ⚠ same locus), [[KLRC2]] (+0.89, fdr 7e-06, ⚠ same locus), [[CXXC4]] (+0.68, fdr 7e-06), [[NR4A3]] (+0.65, fdr 1e-05), [[NR4A2]] (+0.62, fdr 1e-05); moves opposite to [[POP1]] (-0.51, fdr 3e-05), [[NEIL2]] (-0.48, fdr 1e-04), [[ADPGK]] (-0.48, fdr 3e-05).
> It is in [[Module 223]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[KLRC3]] → it (grade C ⚠); 22 go from it, the strongest it → cells under [[Econazole (drug)]] 0.5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13139.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.36×** | +17.5 | 0e+00 | 12/15 (NCI-H23, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.71×** | +12.4 | 9e-33 | 2/2 (NCI-H2030, SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.72×** | +10.5 | 3e-23 | 1/5 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.57×** | +9.4 | 8e-19 | 2/7 (NCI-H23, AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.46×** | +9.4 | 8e-19 | 10/19 (HepG2/C3A, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.69×** | +7.3 | 3e-11 | 8/15 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +7.1 | 7e-11 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.21×** | +5.8 | 4e-07 | 7/14 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.68×** | +5.4 | 6e-06 | 3/19 (NCI-H2030, SW 900, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.11×** | +5.3 | 7e-06 | 5/18 (BT-474, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.91×** | +4.8 | 1e-04 | 10/19 (NCI-H23, A-427, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.11×** | +3.9 | 0.004 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.69×** | +3.8 | 0.005 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +3.7 | 0.009 | 1/14 (NCI-H2030) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +3.4 | 0.026 | 2/10 (HepG2/C3A, SNU-1) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Silodosin (drug)]] 5 µM |  | **1.59×** | +3.2 | 0.041 | 2/10 (NCI-H1573, SHP-77) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.044 | 3/19 (AsPC-1, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.061 | 0/14 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13139.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Daptomycin (drug)]] 0.5 µM in 1 line (NCI-H23 0.114×; ⚠ unreliable plate only); [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 0.0988×); [[Bortezomib (drug)]] 0.05 µM in 1 line (SW 900 0.0778×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.539×** | -4.6 | 0.002 | 12/19 (SW 900, NCI-H2030, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.608× | -3.5 | 0.12 | 13/16 (SW 900, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Mebendazole (drug)]] 5 µM |  | 0.635× | -3.3 | 0.17 | 6/17 (AsPC-1, SK-MEL-2, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.650× | -3.2 | 0.17 | 10/18 (A-427, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13139. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 29.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +11.4) | [[Daptomycin (drug)]] 0.5 µM 0.114× (z -10.4) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 15.6 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0778× (z -8.9) |
| [[A-427 (line)]] | wt | 19.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.30× (z +10.1) | — |
| [[BT-474 (line)]] | alt | 1.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 124× (z +10.3) | — |
| [[HepG2_C3A (line)]] | wt | 4.42 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.6× (z +10.3) | — |
| [[SW480 (line)]] | alt | 3.57 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0988× (z -9.1) |
| [[A-172 (line)]] | wt | 0.322 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.305 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.390 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.408 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.370 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.357 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.390 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.396 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.709 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.289 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.384 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.435 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.358 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.255 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.355 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.321 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.325 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.680 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.725 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13139), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLRC4-KLRK1]] | +0.95 | +0.96 / +0.91 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[KLRC3]] | +0.90 | +0.92 / +0.84 | both halves | 7e-06 | same gene group; STRING 878; ⚠ same locus (20.4 kb, same strand: neighbours can correlate without regulation) |
| [[KLRC2]] | +0.89 | +0.91 / +0.84 | both halves | 7e-06 | same gene group; pathway: DAP12 interactions; STRING 931; ⚠ same locus (35.0 kb, same strand: neighbours can correlate without regulation) |
| [[CXXC4]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[NR4A3]] | +0.65 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[NR4A2]] | +0.62 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[BMP5]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[ID4]] | +0.59 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[ZFHX2]] | +0.57 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[MAP3K2-DT]] | +0.55 | +0.59 / +0.37 | both halves | 9e-05 |  |
| [[CCDC148]] | +0.55 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[GNG4]] | +0.52 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[CFAP300]] | +0.52 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[CA11]] | +0.52 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[LINC01239]] | +0.51 | +0.46 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POP1]] | -0.51 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[NEIL2]] | -0.48 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[ADPGK]] | -0.48 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[RAP1GDS1]] | -0.48 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[SORD]] | -0.47 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[RABEPK]] | -0.46 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[WDR5]] | -0.46 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[HMOX2]] | -0.45 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[SLC15A4]] | -0.45 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[SGTB]] | -0.45 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[SVIL-AS1-1]] | -0.44 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[CRYL1]] | -0.44 | -0.40 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLRC3]] | C | KLRC3 activity raises KLRK1's level | lines that do not express KLRC3 (27) vs lines expressing it (23) | 3.72× lower at baseline in the lines without KLRC3 | 3e-04 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4; co-absent with the target |
| [[KLRC2]] | C | KLRC2 activity raises KLRK1's level | lines that do not express KLRC2 (27) vs lines expressing it (23) | 3.37× lower at baseline in the lines without KLRC2 | 0.002 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRK1, TRPM2-AS; co-absent with the target |
| [[IGFL4]] | C | IGFL4 activity raises KLRK1's level | lines that do not express IGFL4 (25) vs lines expressing it (25) | 2.28× lower at baseline in the lines without IGFL4 | 0.051 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 19, C 3. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Econazole (drug)]] 0.5 µM | B | [[KLRC4-KLRK1]], KLRK1 activity raises the cells' numbers under Econazole 0.5 µM (protects the cells) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 0.83× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| cells under [[Riluzole hydrochloride (drug)]] 0.05 µM | B | [[KLRC4-KLRK1]], KLRK1 activity raises the cells' numbers under Riluzole hydrochloride 0.05 µM (protects the cells) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 0.86× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| [[LINC01091]] | B | [[KLRC4-KLRK1]], KLRK1 activity raises LINC01091's level | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (21) | 2.23× lower at baseline in the lines without KLRC4-KLRK1, KLRK1 | 0.030 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| [[LRRC56]] | B | KLRK1 activity raises LRRC56's level | lines that do not express KLRK1 (29) vs lines expressing it (21) | 1.27× lower at baseline in the lines without KLRK1 | 0.050 | ⚠ within organs, on part of the lines; co-absent genes; also absent: KLRC3, KLRC2, PIP5K1B |
| cells under [[Loperamide (hydrochloride) (drug)]] 0.5 µM | B | [[KLRC4-KLRK1]], KLRK1 activity raises the cells' numbers under Loperamide (hydrochloride) 0.5 µM (protects the cells) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 0.86× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| cells under [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM | B | [[KLRC4-KLRK1]], KLRK1 activity lowers the cells' numbers under Sivelestat (sodium tetrahydrate) 0.5 µM (makes them more sensitive) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 1.18× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| cells under [[Rutin (trihydrate) (drug)]] 0.05 µM | B | [[KLRC4-KLRK1]], KLRK1 activity raises the cells' numbers under Rutin (trihydrate) 0.05 µM (protects the cells) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 0.85× the cells of the other lines | 0.062 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| [[PPP1R1C]] | B | [[KLRC4-KLRK1]], KLRK1 activity raises PPP1R1C's level | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (21) | 1.72× lower at baseline in the lines without KLRC4-KLRK1, KLRK1 | 0.068 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| cells under [[Bendamustine (drug)]] 5 µM | B | [[KLRC4-KLRK1]], KLRK1 activity lowers the cells' numbers under Bendamustine 5 µM (makes them more sensitive) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 1.18× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| cells under [[Fenofibrate (drug)]] 0.05 µM | B | [[KLRC4-KLRK1]], KLRK1 activity raises the cells' numbers under Fenofibrate 0.05 µM (protects the cells) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 0.81× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| cells under [[Almonertinib (hydrochloride) (drug)]] 0.5 µM | B | [[KLRC4-KLRK1]], KLRK1 activity lowers the cells' numbers under Almonertinib (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 1.14× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| cells under [[(S)-Crizotinib (drug)]] 0.05 µM | B | [[KLRC4-KLRK1]], KLRK1 activity raises the cells' numbers under (S)-Crizotinib 0.05 µM (protects the cells) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 0.85× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |

## Where it sits

- **Module**: [[Module 223]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.920). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.4, 33.6); signed map (51.3, 19.9). **Vector** length 45.2, 10.6% of its response variance represented; |z| ≥ 3 in 507 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +9.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +17.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +10.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +9.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +5.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +4.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.1 | +2.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.1 | +1.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.4 | -1.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | killer cell lectin like receptor K1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.2 — chr12:10,372,353-10,391,874 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NKG2D, KLR, NKG2-D, CD314; previously D12S2489E |
| Gene groups (HGNC) | CD molecules; Killer cell lectin like receptors; C-type lectin domain containing |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Reactome | 5 pathways, smallest: DAP12 signaling; DAP12 interactions; Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell |
| Matched by | ensembl_id |

**Function**, from UniProt [P26718](https://www.uniprot.org/uniprotkb/P26718) (NKG2-D type II integral membrane protein):

> Functions as an activating and costimulatory receptor involved in immunosurveillance upon binding to various cellular stress-inducible ligands displayed at the surface of autologous tumor cells and virus-infected cells. Provides both stimulatory and costimulatory innate immune responses on activated killer (NK) cells, leading to cytotoxic activity. Acts as a costimulatory receptor for T-cell receptor (TCR) in CD8(+) T-cell-mediated adaptive immune responses by amplifying T-cell activation. …

**Summary**, from NCBI Gene [22914](https://www.ncbi.nlm.nih.gov/gene/22914):

> Natural killer (NK) cells are lymphocytes that can mediate lysis of certain tumor cells and virus-infected cells without previous activation. They can also regulate specific humoral and cell-mediated immunity. NK cells preferentially express several calcium-dependent (C-type) lectins, which have been implicated in the regulation of NK cell function. The NKG2 gene family is located within the NK complex, a region that contains several C-type lectin genes preferentially expressed in NK cells. …

**Accessions** — [HGNC:18788](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18788) · Entrez [22914](https://www.ncbi.nlm.nih.gov/gene/22914) · UniProt [P26718](https://www.uniprot.org/uniprotkb/P26718) · Ensembl [ENSG00000213809](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213809)

## Data

Gene col 13139: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13139); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13139, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13139]; `tensor/DDL_lfc|DDL_z.npy` [13139]; `embed/gene_vectors.npy` [13139]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13139 or target_col == 13139). Every well: [[KLRK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLRK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
