---
symbol: "LRRK2"
type: "gene"
col: 12063
ensembl_id: "ENSG00000188906"
name: "leucine rich repeat kinase 2"
location: "12q12"
module: 10
arm: "+"
pooled_cpm: 5.33
n_lines_expressing: 25
n_dd_up: 17
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 9
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# LRRK2

*leucine rich repeat kinase 2* — 12q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.57× (z +12.0, q 3e-30, up in 4 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.71× (z +7.1, q 2e-10, up in 10 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.537× (z -5.8, q 3e-06, down in 13 of 23 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.05 µM: 0.664× (z -3.9, q 0.016, down in 10 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (NCI-H1792 0.0453×, A549 0.175×; ⚠ cell-cycle shift, explains ~35% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H1792 0.0603×, SK-MEL-2 0.107×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (A549 0.127×, NCI-H1792 0.0917×; ⚠ cell-cycle shift, explains ~37% of this change).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01725]] (+0.63, fdr 1e-05), [[EIF1B-AS1]] (+0.59, fdr 2e-05), [[LINC01013]] (+0.59, fdr 1e-05); moves opposite to [[SLCO4A1]] (-0.46, fdr 7e-05), [[MPG]] (-0.45, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 9 go from it, the strongest it → [[CSGALNACT1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12063.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.57×** | +12.0 | 3e-30 | 4/13 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.63×** | +11.6 | 7e-29 | 6/8 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.15×** | +10.0 | 4e-21 | 3/9 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.71×** | +7.1 | 2e-10 | 10/22 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +5.8 | 7e-07 | 5/20 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.48×** | +5.2 | 2e-05 | 6/22 (SK-MEL-2, NCI-H23, …) | top dose only | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +5.0 | 6e-05 | 12/22 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +4.8 | 1e-04 | 3/15 (RPMI-7951, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.6 | 3e-04 | 2/14 (NCI-H460, C32) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +4.3 | 0.001 | 1/22 (A498) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.40×** | +3.9 | 0.004 | 12/22 (HEC-1-A, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.45×** | +3.7 | 0.009 | 8/22 (HEC-1-A, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.023 | 14/22 (HEC-1-A, A549, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.67×** | +3.4 | 0.023 | 1/19 (RPMI-7951) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.47×** | +3.4 | 0.023 | 6/22 (HEC-1-A, CFPAC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.073 | 4/22 (NCI-H1792, HEC-1-A, …) | rises with dose |  |
| [[ERK5-IN-2 (drug)]] 0.5 µM |  | **1.58×** | +3.1 | 0.073 | 0/20 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12063.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (NCI-H1792 0.0453×, A549 0.175×; ⚠ cell-cycle shift, explains ~35% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H1792 0.0603×, SK-MEL-2 0.107×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (A549 0.127×, NCI-H1792 0.0917×; ⚠ cell-cycle shift, explains ~37% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.537×** | -5.8 | 3e-06 | 13/23 (A549, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.573×** | -5.2 | 5e-05 | 15/23 (A549, J82, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.645×** | -4.1 | 0.007 | 15/23 (NCI-H1792, NCI-H2030, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.664×** | -3.9 | 0.016 | 10/23 (NCI-H1792, J82, …) | all doses, flat | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.680×** | -3.6 | 0.030 | 10/22 (NCI-H1792, A549, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.682×** | -3.6 | 0.030 | 9/21 (NCI-H1573, A-172, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.690×** | -3.5 | 0.038 | 15/23 (A549, NCI-H1792, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.716× | -3.1 | 0.12 | 4/23 (NCI-H23, HEC-1-A, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12063. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 9.56 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0453× (z -13.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A549 (line)]] | wt | 32.9 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.127× (z -10.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[C32 (line)]] | wt | 54.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 19.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.565 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.587 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.592 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.889 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.657 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.540 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.536 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.492 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.559 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.639 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.943 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.618 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.738 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.660 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.504 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12063), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01725]] | +0.63 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[EIF1B-AS1]] | +0.59 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[LINC01013]] | +0.59 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[FRG1-DT]] | +0.57 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[NLGN1]] | +0.56 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[LINC00648]] | +0.56 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[STPG2]] | +0.56 | +0.50 / +0.30 | both halves | 2e-04 |  |
| [[MSC-AS1]] | +0.55 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[L3MBTL4]] | +0.55 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[TIMD4]] | +0.55 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[HAVCR1]] | +0.55 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[RNLS]] | +0.55 | +0.41 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLCO4A1]] | -0.46 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[MPG]] | -0.45 | -0.42 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises LRRK2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC00278]] | C | LINC00278 activity raises LRRK2's level | lines that do not express LINC00278 (32) vs lines expressing it (18) | 2.03× lower at baseline in the lines without LINC00278 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZFY, PRKY, RPS4Y1; co-absent with the target |
| [[MSC-AS1]] | C | MSC-AS1 activity raises LRRK2's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 3.27× lower at baseline in the lines without MSC-AS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2; co-absent with the target |
| [[TBX18]] | C | TBX18 activity raises LRRK2's level | lines that do not express TBX18 (27) vs lines expressing it (23) | 2.80× lower at baseline in the lines without TBX18 | 0.025 | ⚠ within organs, on part of the lines; also absent: SFRP1, LRRK2, ENSG00000286251; co-absent with the target |
| [[ZFHX4]] | C | ZFHX4 activity raises LRRK2's level | lines that do not express ZFHX4 (23) vs lines expressing it (27) | 2.84× lower at baseline in the lines without ZFHX4 | 0.032 | ⚠ within organs, on part of the lines; also absent: SNCA, UCHL1, SLITRK5; co-absent with the target |
| [[TIMD4]] | C | TIMD4 activity raises LRRK2's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 2.02× lower at baseline in the lines without TIMD4 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSGALNACT1]] | C | LRRK2 activity raises CSGALNACT1's level | lines that do not express LRRK2 (25) vs lines expressing it (25) | 3.17× lower at baseline in the lines without LRRK2 | 0.023 | ⚠ within organs, on part of the lines; also absent: FAM110B, GFRA1, ADAMTS1; co-absent with the target |
| [[EYA4]] | C | LRRK2 activity raises EYA4's level | lines that do not express LRRK2 (25) vs lines expressing it (25) | 4.37× lower at baseline in the lines without LRRK2 | 0.025 | ⚠ within organs, on part of the lines; also absent: FAM110B, GFRA1, ADAMTS1; co-absent with the target |
| [[LINC00278]] | C | LRRK2 activity raises LINC00278's level | lines that do not express LRRK2 (25) vs lines expressing it (25) | 1.77× lower at baseline in the lines without LRRK2 | 0.032 | ⚠ within organs, on part of the lines; also absent: FAM110B, GFRA1, ADAMTS1; co-absent with the target |
| [[ANKRD18B]] | C | LRRK2 activity raises ANKRD18B's level | lines that do not express LRRK2 (25) vs lines expressing it (25) | 2.66× lower at baseline in the lines without LRRK2 | 0.035 | ⚠ within organs, on part of the lines; also absent: FAM110B, GFRA1, ADAMTS1; co-absent with the target |
| [[TBX18]] | C | LRRK2 activity raises TBX18's level | lines that do not express LRRK2 (25) vs lines expressing it (25) | 4.34× lower at baseline in the lines without LRRK2 | 0.035 | ⚠ within organs, on part of the lines; also absent: FAM110B, GFRA1, ADAMTS1; co-absent with the target |
| [[LRAT]] | C | LRRK2 activity raises LRAT's level | lines that do not express LRRK2 (25) vs lines expressing it (25) | 3.73× lower at baseline in the lines without LRRK2 | 0.040 | ⚠ within organs, on part of the lines; also absent: FAM110B, GFRA1, ADAMTS1; co-absent with the target |
| [[HORMAD1]] | C | LRRK2 activity raises HORMAD1's level | lines that do not express LRRK2 (25) vs lines expressing it (25) | 1.91× lower at baseline in the lines without LRRK2 | 0.063 | ⚠ within organs, on part of the lines; also absent: FAM110B, GFRA1, ADAMTS1; co-absent with the target |
| [[RNF180]] | C | LRRK2 activity raises RNF180's level | lines that do not express LRRK2 (25) vs lines expressing it (25) | 3.18× lower at baseline in the lines without LRRK2 | 0.063 | ⚠ within organs, on part of the lines; also absent: FAM110B, GFRA1, ADAMTS1; co-absent with the target |
| [[KYNU]] | C | LRRK2 activity raises KYNU's level | lines that do not express LRRK2 (25) vs lines expressing it (25) | 4.26× lower at baseline in the lines without LRRK2 | 0.072 | ⚠ within organs, on part of the lines; also absent: FAM110B, GFRA1, ADAMTS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.471). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (44.5, 25.8); signed map (36.2, 40.0). **Vector** length 53.4, 12.4% of its response variance represented; |z| ≥ 3 in 593 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +10.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +7.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +3.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -2.4 | -3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -2.1 | -5.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -1.8 | -5.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | -1.6 | -3.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -2.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -1.9 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q12 — chr12:40,196,744-40,369,285 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ROCO2, DKFZp434H2111, FLJ45829, RIPK7; previously PARK8 |
| Gene groups (HGNC) | ROCO family; Armadillo like helical domain containing; Leucine rich repeat kinase family |
| Reactome | 3 pathways, smallest: PTK6 promotes HIF1A stabilization; Signaling by Non-Receptor Tyrosine Kinases; Signaling by PTK6 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5S007](https://www.uniprot.org/uniprotkb/Q5S007) (Leucine-rich repeat serine/threonine-protein kinase 2):

> Serine/threonine-protein kinase which phosphorylates a broad range of proteins involved in multiple processes such as neuronal plasticity, innate immunity, autophagy, and vesicle trafficking. Is a key regulator of RAB GTPases by regulating the GTP/GDP exchange and interaction partners of RABs through phosphorylation. Phosphorylates RAB3A, RAB3B, RAB3C, RAB3D, RAB5A, RAB5B, RAB5C, RAB8A, RAB8B, RAB10, RAB12, RAB29, RAB35, and RAB43. Regulates the RAB3IP-catalyzed GDP/GTP exchange for RAB8A …

**Summary**, from NCBI Gene [120892](https://www.ncbi.nlm.nih.gov/gene/120892):

> This gene is a member of the leucine-rich repeat kinase family and encodes a protein with an ankryin repeat region, a leucine-rich repeat (LRR) domain, a kinase domain, a DFG-like motif, a RAS domain, a GTPase domain, a MLK-like domain, and a WD40 domain. The protein is present largely in the cytoplasm but also associates with the mitochondrial outer membrane. Mutations in this gene have been associated with Parkinson disease-8. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18618](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18618) · Entrez [120892](https://www.ncbi.nlm.nih.gov/gene/120892) · UniProt [Q5S007](https://www.uniprot.org/uniprotkb/Q5S007) · Ensembl [ENSG00000188906](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188906)

## Data

Gene col 12063: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12063); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12063, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12063]; `tensor/DDL_lfc|DDL_z.npy` [12063]; `embed/gene_vectors.npy` [12063]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12063 or target_col == 12063). Every well: [[LRRK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
