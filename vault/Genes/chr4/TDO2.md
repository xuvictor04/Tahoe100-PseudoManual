---
symbol: "TDO2"
type: "gene"
col: 7567
ensembl_id: "ENSG00000151790"
name: "tryptophan 2,3-dioxygenase"
location: "4q32.1"
module: 117
arm: "+"
pooled_cpm: 6.01
n_lines_expressing: 23
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 11
direction_downstream: 9
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# TDO2

*tryptophan 2,3-dioxygenase* — 4q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.49× (z +9.4, q 5e-18, up in 3 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 2.57× (z +7.1, q 3e-10, up in 12 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.373× (z -7.4, q 8e-11, down in 20 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EGF]] (+0.64, fdr 1e-05), [[MAP1A]] (+0.61, fdr 1e-05), [[CYP39A1]] (+0.60, fdr 1e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[LYPLAL1-DT]] → it (grade C ⚠); 9 go from it, the strongest it → [[MAP1A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7567.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.49×** | +9.4 | 5e-18 | 3/14 (SW48, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.21×** | +8.4 | 1e-14 | 1/7 (NCI-H1792) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.57×** | +7.1 | 3e-10 | 12/20 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.37×** | +6.0 | 3e-07 | 3/11 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.30×** | +5.9 | 4e-07 | 12/21 (NCI-H1573, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.82×** | +4.5 | 7e-04 | 10/20 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.004 | 6/21 (hTERT-HPNE, A498, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.65×** | +3.7 | 0.013 | 8/21 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.63×** | +3.7 | 0.015 | 10/21 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.66×** | +3.6 | 0.015 | 11/20 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **2.48×** | +3.6 | 0.019 | 2/12 (LoVo, NCI-H1573) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.82×** | +3.2 | 0.066 | 1/13 (NCI-H1573) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.50× | +3.0 | 0.10 | 12/20 (SW 900, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7567.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.373×** | -7.4 | 8e-11 | 20/21 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.428×** | -6.4 | 6e-08 | 16/20 (LoVo, RPMI-7951, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.451×** | -6.0 | 4e-07 | 14/20 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.465×** | -5.7 | 1e-06 | 16/20 (SW48, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.650×** | -4.6 | 6e-04 | 15/19 (NCI-H1573, NCI-H460, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.583×** | -4.0 | 0.005 | 11/18 (NCI-H1792, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.546×** | -3.4 | 0.049 | 8/21 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.728×** | -3.4 | 0.049 | 14/21 (H4, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.629×** | -3.3 | 0.049 | 11/17 (NCI-H460, RPMI-7951, …) | rises with dose | composition shift; position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.641×** | -3.3 | 0.049 | 9/20 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.649×** | -3.2 | 0.061 | 15/18 (NCI-H1792, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7567. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 15.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0766× (z -16.4) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -12.3) |
| [[NCI-H1573 (line)]] | alt | 21.2 | 2 | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 8.18× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.0678× (z -16.6) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0838× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 21.1 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0409× (z -13.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -12.2) |
| [[LoVo (line)]] | wt | 10.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -13.0) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.109× (z -9.7) |
| [[A-172 (line)]] | wt | 28.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0981× (z -9.6) |
| [[A498 (line)]] | wt | 26.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -12.0) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -9.9) |
| [[SW48 (line)]] | wt | 49.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0770× (z -12.0) |
| [[H4 (line)]] | wt | 12.6 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0561× (z -8.9) |
| [[SHP-77 (line)]] | alt | 3.68 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0556× (z -11.7) ⚠ cell-cycle shift, explains ~75% of this change |
| [[SW 900 (line)]] | alt | 9.87 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0697× (z -12.0) ⚠ cell-cycle shift, explains ~75% of this change |
| [[A-427 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.647 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.583 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.744 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.705 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.594 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.500 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.961 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.77 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.514 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.658 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.560 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.880 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.509 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7567), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGF]] | +0.64 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[MAP1A]] | +0.61 | +0.62 / +0.49 | both halves | 1e-05 | **novel candidate** |
| [[CYP39A1]] | +0.60 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[CACNA2D3]] | +0.60 | +0.62 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[VEGFD]] | +0.58 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[TRIM16L]] | +0.57 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[PRKACB]] | +0.57 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[MIR3171HG]] | +0.56 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[NMRAL2P]] | +0.56 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[SSX1]] | +0.56 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[DGKG]] | +0.56 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[CYP4F11]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LYPLAL1-DT]] | C | LYPLAL1-DT activity raises TDO2's level | lines that do not express LYPLAL1-DT (32) vs lines expressing it (18) | 2.35× lower at baseline in the lines without LYPLAL1-DT | 0.005 | ⚠ within organs, on part of the lines; also absent: EBF1, ANXA10, IRF4; maybe low, not absent; co-absent with the target |
| [[MIR3171HG]] | C | MIR3171HG activity raises TDO2's level | lines that do not express MIR3171HG (33) vs lines expressing it (17) | 2.53× lower at baseline in the lines without MIR3171HG | 0.023 | ⚠ within organs, on part of the lines; also absent: LINC02616, IL13RA2, MSC; co-absent with the target |
| [[MSC-AS1]] | C | MSC-AS1 activity raises TDO2's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 2.86× lower at baseline in the lines without MSC-AS1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2; co-absent with the target |
| [[KRT14]] | C | KRT14 activity raises TDO2's level | lines that do not express KRT14 (43) vs lines expressing it (7) | 2.78× lower at baseline in the lines without KRT14 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230258, DSG4, SPINK13; co-absent with the target |
| [[C5orf46]] | C | C5orf46 activity raises TDO2's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 2.80× lower at baseline in the lines without C5orf46 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[CHSY3]] | C | CHSY3 activity raises TDO2's level | lines that do not express CHSY3 (23) vs lines expressing it (27) | 2.31× lower at baseline in the lines without CHSY3 | 0.064 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, ZNF365, GBP5; co-absent with the target |
| [[ITGA4]] | C | ITGA4 activity raises TDO2's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 2.70× lower at baseline in the lines without ITGA4 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[TRPA1]] | C | TRPA1 activity raises TDO2's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 2.24× lower at baseline in the lines without TRPA1 | 0.072 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; co-absent with the target |
| [[GREM2]] | C | GREM2 activity raises TDO2's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 2.15× lower at baseline in the lines without GREM2 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054; co-absent with the target |
| [[BHMT2]] | C | BHMT2 activity raises TDO2's level | lines that do not express BHMT2 (40) vs lines expressing it (10) | 2.14× lower at baseline in the lines without BHMT2 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, LINC01320, CP; co-absent with the target |
| [[CACNA2D3]] | C | CACNA2D3 activity raises TDO2's level | lines that do not express CACNA2D3 (36) vs lines expressing it (14) | 2.74× lower at baseline in the lines without CACNA2D3 | 0.0997 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NCAM1, LINC01287, LINC00824; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP1A]] | B | TDO2 activity raises MAP1A's level | lines that do not express TDO2 (27) vs lines expressing it (23) | 2.97× lower at baseline in the lines without TDO2 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LAMA1, SCN3A, MSC-AS1 |
| [[ARHGEF6]] | B | TDO2 activity raises ARHGEF6's level | lines that do not express TDO2 (27) vs lines expressing it (23) | 2.22× lower at baseline in the lines without TDO2 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LAMA1, SCN3A, MSC-AS1 |
| [[ATP10D]] | B | TDO2 activity raises ATP10D's level | lines that do not express TDO2 (27) vs lines expressing it (23) | 1.98× lower at baseline in the lines without TDO2 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LAMA1, SCN3A, MSC-AS1 |
| [[PAPPA2]] | C | TDO2 activity raises PAPPA2's level | lines that do not express TDO2 (27) vs lines expressing it (23) | 2.83× lower at baseline in the lines without TDO2 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LAMA1, SCN3A, MSC-AS1; co-absent with the target |
| [[GLIS1]] | C | TDO2 activity raises GLIS1's level | lines that do not express TDO2 (27) vs lines expressing it (23) | 2.90× lower at baseline in the lines without TDO2 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LAMA1, SCN3A, MSC-AS1; co-absent with the target |
| [[ITGA4]] | C | TDO2 activity raises ITGA4's level | lines that do not express TDO2 (27) vs lines expressing it (23) | 3.75× lower at baseline in the lines without TDO2 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LAMA1, SCN3A, MSC-AS1; co-absent with the target |
| [[GLIS3]] | C | TDO2 activity raises GLIS3's level | lines that do not express TDO2 (27) vs lines expressing it (23) | 3.31× lower at baseline in the lines without TDO2 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LAMA1, SCN3A, MSC-AS1; co-absent with the target |
| [[ADGRB3]] | C | TDO2 activity raises ADGRB3's level | lines that do not express TDO2 (27) vs lines expressing it (23) | 2.66× lower at baseline in the lines without TDO2 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LAMA1, SCN3A, MSC-AS1; co-absent with the target |
| [[MSC-AS1]] | C | TDO2 activity raises MSC-AS1's level | lines that do not express TDO2 (27) vs lines expressing it (23) | 5.49× lower at baseline in the lines without TDO2 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LAMA1, SCN3A, MSC-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.643). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-5.1, 50.2); signed map (51.4, -13.3). **Vector** length 56.0, 15.1% of its response variance represented; |z| ≥ 3 in 518 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +4.2 | +7.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +4.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.1 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +1.4 |
| fall | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.7 | -6.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -3.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.4 | -2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.4 | -1.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | tryptophan 2,3-dioxygenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.1 — chr4:155,854,738-155,920,406 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TDO, TPH2 |
| Gene groups (HGNC) | Oxygenases |
| Hallmark sets | FATTY_ACID_METABOLISM, XENOBIOTIC_METABOLISM |
| Reactome | 2 pathways, smallest: Tryptophan catabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P48775](https://www.uniprot.org/uniprotkb/P48775) (Tryptophan 2,3-dioxygenase):

> Heme-dependent dioxygenase that catalyzes the oxidative cleavage of the L-tryptophan (L-Trp) pyrrole ring and converts L-tryptophan to N-formyl-L-kynurenine. Catalyzes the oxidative cleavage of the indole moiety.

**Summary**, from NCBI Gene [6999](https://www.ncbi.nlm.nih.gov/gene/6999):

> This gene encodes a heme enzyme that plays a critical role in tryptophan metabolism by catalyzing the first and rate-limiting step of the kynurenine pathway. Increased activity of the encoded protein and subsequent kynurenine production may also play a role in cancer through the suppression of antitumor immune responses, and single nucleotide polymorphisms in this gene may be associated with autism. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:11708](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11708) · Entrez [6999](https://www.ncbi.nlm.nih.gov/gene/6999) · UniProt [P48775](https://www.uniprot.org/uniprotkb/P48775) · Ensembl [ENSG00000151790](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151790)

## Data

Gene col 7567: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7567); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7567, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7567]; `tensor/DDL_lfc|DDL_z.npy` [7567]; `embed/gene_vectors.npy` [7567]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7567 or target_col == 7567). Every well: [[TDO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TDO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
