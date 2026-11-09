---
symbol: "EBF1"
type: "gene"
col: 8931
ensembl_id: "ENSG00000164330"
name: "EBF transcription factor 1"
location: "5q33.3"
module: 121
arm: "+"
pooled_cpm: 26.32
n_lines_expressing: 20
n_dd_up: 27
n_dd_down: 3
n_dd_up_clean: 23
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 15
direction_downstream: 18
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# EBF1

*EBF transcription factor 1* — 5q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.40× (z +15.9, q 0e+00, up in 4 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.743× (z -3.9, q 0.066, down in 9 of 18 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Mebendazole (drug)]] 5 µM: 0.745× (z -3.7, q 0.072, down in 7 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1573 0.237×, NCI-H460 0.310×, A498 0.301×; ⚠ toxic; transcription drop); [[Betamethasone dipropionate (drug)]] 5 µM in 1 line (NCI-H1573 0.157×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 0.179×; ⚠ toxic; cell-cycle shift, explains ~90% of this change); [[Triamcinolone (drug)]] 0.5 µM in 1 line (NCI-H1573 0.209×); [[Triamcinolone (drug)]] 5 µM in 1 line (NCI-H1573 0.369×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KYNU]] (+0.65, fdr 1e-05), [[TEX41]] (+0.64, fdr 1e-05), [[MSR1]] (+0.61, fdr 2e-05); moves opposite to [[SRD5A1]] (-0.52, fdr 3e-05), [[PRMT7]] (-0.50, fdr 4e-05), [[THOC3]] (-0.50, fdr 6e-05).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[EPHA7]] → it (grade B ⚠); 18 go from it, the strongest it → [[THOC3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8931.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +15.9 | 0e+00 | 4/17 (LOX-IMVI, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.00×** | +12.6 | 5e-34 | 11/18 (SNU-423, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.50×** | +11.8 | 6e-30 | 1/17 (LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.72×** | +9.9 | 6e-21 | 13/17 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.87×** | +8.0 | 1e-13 | 13/18 (SK-MEL-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.94×** | +8.0 | 1e-13 | 15/18 (A-172, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.86×** | +8.0 | 1e-13 | 11/18 (A-172, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.86×** | +8.0 | 1e-13 | 10/18 (A-172, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +6.8 | 5e-10 | 7/18 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.73×** | +6.8 | 6e-10 | 13/18 (NCI-H1573, SNU-423, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +6.8 | 6e-10 | 7/18 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.51×** | +5.1 | 1e-05 | 1/15 (LOX-IMVI) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.0 | 2e-05 | 5/18 (A-172, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +4.8 | 6e-05 | 12/17 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +4.7 | 8e-05 | 12/18 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +4.6 | 1e-04 | 2/18 (CHP-212, SNU-423) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.3 | 5e-04 | 0/17 | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +4.3 | 5e-04 | 11/18 (A-172, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~17% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8931.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1573 0.237×, NCI-H460 0.310×, A498 0.301×; ⚠ toxic; transcription drop); [[Betamethasone dipropionate (drug)]] 5 µM in 1 line (NCI-H1573 0.157×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 0.179×; ⚠ toxic; cell-cycle shift, explains ~90% of this change); [[Triamcinolone (drug)]] 0.5 µM in 1 line (NCI-H1573 0.209×); [[Triamcinolone (drug)]] 5 µM in 1 line (NCI-H1573 0.369×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.743×** | -3.9 | 0.066 | 9/18 (NCI-H460, HS-578T, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.745×** | -3.7 | 0.072 | 7/18 (NCI-H460, H4, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.824×** | -3.6 | 0.072 | 12/18 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.05 µM |  | 0.764× | -3.3 | 0.14 | 4/18 (A-172, NCI-H1792, …) | inconsistent across doses |  |
| [[Tazarotene (drug)]] 5 µM |  | 0.785× | -3.1 | 0.18 | 6/18 (SNU-423, C32, …) | top dose only | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | 0.844× | -3.1 | 0.18 | 4/18 (NCI-H1573, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8931. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 103 | 2 | 8 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.91× (z +10.9) | [[Betamethasone dipropionate (drug)]] 5 µM 0.157× (z -12.2) |
| [[A-172 (line)]] | wt | 19.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.49× (z +15.1) | — |
| [[NCI-H460 (line)]] | wt | 85.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -9.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 24.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +10.7) | — |
| [[A498 (line)]] | wt | 69.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -8.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 199 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +9.6) | — |
| [[A-427 (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.48 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 169 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 53.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.17 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.49 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 144 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.90 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.44 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.40 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.73 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8931), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KYNU]] | +0.65 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[TEX41]] | +0.64 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[MSR1]] | +0.61 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[NOVA1]] | +0.61 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[ARHGAP24]] | +0.61 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[NRG1]] | +0.59 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[EYA4]] | +0.58 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[DOCK10]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[HECW2]] | +0.58 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[LRP1B]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[PIEZO2]] | +0.58 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[CYP1B1]] | +0.58 | +0.48 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRD5A1]] | -0.52 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[PRMT7]] | -0.50 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[THOC3]] | -0.50 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[ZDHHC9]] | -0.50 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[EXD2]] | -0.49 | -0.58 / -0.36 | both halves | 9e-05 |  |
| [[CRLS1]] | -0.48 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[PMS2P3]] | -0.47 | -0.44 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 1, C 14. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA7]] | B | EPHA7 activity lowers EBF1's level | lines that do not express EPHA7 (30) vs lines expressing it (20) | 1.24× higher at baseline in the lines without EPHA7 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000287683, GRIA2, NTNG1 |
| [[MSC]] | C | MSC activity raises EBF1's level | lines that do not express MSC (34) vs lines expressing it (16) | 7.95× lower at baseline in the lines without MSC | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |
| [[MSC-AS1]] | C | MSC-AS1 activity raises EBF1's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 6.98× lower at baseline in the lines without MSC-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2; co-absent with the target |
| [[RSPO3]] | C | RSPO3 activity raises EBF1's level | lines that do not express RSPO3 (39) vs lines expressing it (11) | 4.43× lower at baseline in the lines without RSPO3 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2; co-absent with the target |
| [[FYB1]] | C | FYB1 activity raises EBF1's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 3.45× lower at baseline in the lines without FYB1 | 0.025 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450; co-absent with the target |
| [[TMEM178B]] | C | TMEM178B activity raises EBF1's level | lines that do not express TMEM178B (22) vs lines expressing it (28) | 3.54× lower at baseline in the lines without TMEM178B | 0.026 | ⚠ within organs, on part of the lines; also absent: NTRK3, SPOCK1, POU3F2; co-absent with the target |
| [[LINC01687]] | C | LINC01687 activity raises EBF1's level | lines that do not express LINC01687 (31) vs lines expressing it (19) | 4.68× lower at baseline in the lines without LINC01687 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC02616, TPTE; co-absent with the target |
| [[DOCK10]] | C | DOCK10 activity raises EBF1's level | lines that do not express DOCK10 (24) vs lines expressing it (26) | 5.80× lower at baseline in the lines without DOCK10 | 0.033 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, TRPA1; co-absent with the target |
| [[CSGALNACT1]] | C | CSGALNACT1 activity raises EBF1's level | lines that do not express CSGALNACT1 (25) vs lines expressing it (25) | 3.85× lower at baseline in the lines without CSGALNACT1 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: BCL2A1, ATP10A, FGF14; co-absent with the target |
| [[EDNRB]] | C | EDNRB activity raises EBF1's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 3.59× lower at baseline in the lines without EDNRB | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[LINC02930]] | C | LINC02930 activity raises EBF1's level | lines that do not express LINC02930 (33) vs lines expressing it (17) | 4.88× lower at baseline in the lines without LINC02930 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000232053, GYPC, PLPP4; co-absent with the target |
| [[EPHA5-AS1]] | C | EPHA5-AS1 activity raises EBF1's level | lines that do not express EPHA5-AS1 (28) vs lines expressing it (22) | 4.63× lower at baseline in the lines without EPHA5-AS1 | 0.071 | ⚠ within organs, on part of the lines; also absent: EPHA5, ADAM23, TRPC4; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 5, C 13. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THOC3]] | B | EBF1 activity lowers THOC3's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 1.35× higher at baseline in the lines without EBF1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4 |
| [[LDB2]] | B | EBF1 activity raises LDB2's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 2.65× lower at baseline in the lines without EBF1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4 |
| [[TLR6]] | B | EBF1 activity raises TLR6's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 2.49× lower at baseline in the lines without EBF1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4 |
| [[RMDN2-AS1]] | B | EBF1 activity raises RMDN2-AS1's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 2.10× lower at baseline in the lines without EBF1 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4 |
| [[NR3C1]] | B | EBF1 activity raises NR3C1's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 3.37× lower at baseline in the lines without EBF1 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4 |
| [[DOCK10]] | C | EBF1 activity raises DOCK10's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 7.95× lower at baseline in the lines without EBF1 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4; co-absent with the target |
| [[MSC-AS1]] | C | EBF1 activity raises MSC-AS1's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 9.44× lower at baseline in the lines without EBF1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4; co-absent with the target |
| [[DGKI]] | C | EBF1 activity raises DGKI's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 3.14× lower at baseline in the lines without EBF1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4; co-absent with the target |
| [[RSPO3]] | C | EBF1 activity raises RSPO3's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 3.29× lower at baseline in the lines without EBF1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4; co-absent with the target |
| [[KYNU]] | C | EBF1 activity raises KYNU's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 5.96× lower at baseline in the lines without EBF1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4; co-absent with the target |
| [[MSC]] | C | EBF1 activity raises MSC's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 2.94× lower at baseline in the lines without EBF1 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4; co-absent with the target |
| [[EYA4]] | C | EBF1 activity raises EYA4's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 5.45× lower at baseline in the lines without EBF1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.689). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.6, 24.9); signed map (42.7, 26.8). **Vector** length 67.7, 22.0% of its response variance represented; |z| ≥ 3 in 499 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.6 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.8 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +5.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +1.0 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -0.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | EBF transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.3 — chr5:158,695,920-159,099,916 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OLF1, COE1; previously EBF |
| Gene groups (HGNC) | EBF transcription factors; IPT domain containing |
| Reactome | 5 pathways, smallest: Expression and translocation of olfactory receptors; Olfactory Signaling Pathway; Transcriptional regulation of white adipocyte differentiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UH73](https://www.uniprot.org/uniprotkb/Q9UH73) (Transcription factor COE1):

> Key pioneer transcription factor of B-cell specification and commitment. Recognizes variations of the palindromic sequence 5'-ATTCCCNNGGGAATT-3'. Operates in a transcription factor network to activate B-cell-specific genes and repress genes associated with alternative cell fates. For instance, positively regulates many B-cell specific genes including BCR or CD40 while repressing genes that direct cells into alternative lineages, including GATA3 and TCF7 for the T-cell lineage. In addition to …

**Summary**, from NCBI Gene [1879](https://www.ncbi.nlm.nih.gov/gene/1879):

> Predicted to enable DNA-binding transcription activator activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in positive regulation of transcription by RNA polymerase II. Predicted to act upstream of or within positive regulation of DNA-templated transcription. Predicted to be located in chromatin. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:3126](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3126) · Entrez [1879](https://www.ncbi.nlm.nih.gov/gene/1879) · UniProt [Q9UH73](https://www.uniprot.org/uniprotkb/Q9UH73) · Ensembl [ENSG00000164330](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164330)

## Data

Gene col 8931: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8931); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8931, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8931]; `tensor/DDL_lfc|DDL_z.npy` [8931]; `embed/gene_vectors.npy` [8931]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8931 or target_col == 8931). Every well: [[EBF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EBF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
