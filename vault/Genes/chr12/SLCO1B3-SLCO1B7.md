---
symbol: "SLCO1B3-SLCO1B7"
type: "gene"
col: 15018
ensembl_id: "ENSG00000257046"
name: "SLCO1B3-SLCO1B7 readthrough"
location: "12p12.2"
module: 73
arm: "+"
pooled_cpm: 44.22
n_lines_expressing: 23
n_dd_up: 6
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 11
direction_downstream: 8
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# SLCO1B3-SLCO1B7

*SLCO1B3-SLCO1B7 readthrough* — 12p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.86× (z +9.5, q 2e-18, up in 1 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.49× (z +8.6, q 3e-15, up in 9 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.597× (z -7.9, q 2e-12, down in 18 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLCO1B3]] (+0.84, fdr 7e-06, ⚠ same locus), [[SLCO1B1]] (+0.72, fdr 7e-06, ⚠ same locus), [[NOSTRIN]] (+0.64, fdr 1e-05), [[LINC02582]] (+0.60, fdr 1e-05), [[FBXW10B]] (+0.60, fdr 2e-05); moves opposite to [[FLYWCH2]] (-0.50, fdr 7e-05), [[ZSCAN2]] (-0.49, fdr 1e-04), [[UBAC1]] (-0.48, fdr 4e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 8 go from it, the strongest it → [[ADAM32]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15018.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.86×** | +9.5 | 2e-18 | 1/18 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +8.6 | 3e-15 | 9/21 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +8.3 | 3e-14 | 4/17 (NCI-H2030, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +7.0 | 4e-10 | 11/21 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.4 | 0.001 | 3/21 (A-427, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +4.2 | 0.003 | 0/18 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Demeclocycline (drug)]] 5 µM |  | 1.16× | +3.1 | 0.14 | 10/21 (A-172, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15018.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.597×** | -7.9 | 2e-12 | 18/21 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.655×** | -6.5 | 3e-08 | 17/21 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.721×** | -5.0 | 1e-04 | 14/21 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.837× | -3.9 | 0.016 | 10/21 (CFPAC-1, A549, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.787×** | -3.7 | 0.024 | 15/21 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.789×** | -3.6 | 0.024 | 10/21 (HS-578T, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.636×** | -3.6 | 0.024 | 11/21 (KATO III, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.850× | -3.5 | 0.028 | 15/21 (RKO, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15018. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 195 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -24.1) |
| [[LoVo (line)]] | wt | 359 | 2 | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.146× (z -15.9) |
| [[LS 180 (line)]] | wt | 191 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.107× (z -18.5) |
| [[A549 (line)]] | wt | 142 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -18.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.337× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 92.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.190× (z -12.9) |
| [[MIA PaCa-2 (line)]] | alt | 82.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 8.30× (z +14.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.182× (z -11.4) ⚠ toxic; cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 102 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.175× (z -12.3) |
| [[A-427 (line)]] | wt | 34.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.51× (z +9.6) | [[Harringtonine (drug)]] 5 µM 0.200× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 128 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0426× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.214× (z -10.3) |
| [[HT-29 (line)]] | alt | 25.9 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.142× (z -11.3) |
| [[RKO (line)]] | wt | 16.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -8.8) |
| [[SW48 (line)]] | wt | 176 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 7.36 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.11 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.13 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.08 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.67 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.42 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 96.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.06 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.59 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.27 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.65 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.21 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.51 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 8.15 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.89 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15018), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLCO1B3]] | +0.84 | +0.82 / +0.87 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[SLCO1B1]] | +0.72 | +0.74 / +0.70 | both halves | 7e-06 | ⚠ same locus (40.9 kb, same strand: neighbours can correlate without regulation) |
| [[NOSTRIN]] | +0.64 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[LINC02582]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[FBXW10B]] | +0.60 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[NPSR1-AS1]] | +0.59 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[HEPH]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[BTBD16]] | +0.57 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[LINC02474]] | +0.57 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[SLC2A9]] | +0.55 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[SPON1]] | +0.55 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[CALB1]] | +0.54 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[MYO16-AS1]] | +0.54 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[CFAP161]] | +0.54 | +0.57 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLYWCH2]] | -0.50 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[ZSCAN2]] | -0.49 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[UBAC1]] | -0.48 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[FBXO44]] | -0.47 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[USP30]] | -0.47 | -0.37 / -0.48 | both halves | 7e-05 |  |
| [[MRI1]] | -0.47 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[HYKK]] | -0.47 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[MAP4K2]] | -0.46 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[MED30]] | -0.46 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[UBTD1]] | -0.46 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[PHC1]] | -0.46 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[KANTR]] | -0.46 | -0.40 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 3, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SLCO1B3-SLCO1B7's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LMO7DN]] | B | LMO7DN activity raises SLCO1B3-SLCO1B7's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 3.18× lower at baseline in the lines without LMO7DN | 0.081 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[MYO16-AS1]] | B | MYO16-AS1 activity raises SLCO1B3-SLCO1B7's level | lines that do not express MYO16-AS1 (23) vs lines expressing it (27) | 3.04× lower at baseline in the lines without MYO16-AS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000275216, KRT18, LAMC2 |
| [[SLCO1B1]] | C | SLCO1B1 activity raises SLCO1B3-SLCO1B7's level | lines that do not express SLCO1B1 (28) vs lines expressing it (22) | 8.01× lower at baseline in the lines without SLCO1B1 | 9e-06 | ⚠ within organs, on part of the lines; also absent: ENSG00000257062, SLCO1B3, SLCO1B3-SLCO1B7; co-absent with the target |
| [[SLCO1B3]] | C | SLCO1B3 activity raises SLCO1B3-SLCO1B7's level | lines that do not express SLCO1B3 (28) vs lines expressing it (22) | 8.81× lower at baseline in the lines without SLCO1B3 | 1e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000257062, SLCO1B3-SLCO1B7, SLCO1B1; co-absent with the target |
| [[TIMD4]] | C | TIMD4 activity raises SLCO1B3-SLCO1B7's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 3.37× lower at baseline in the lines without TIMD4 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA; co-absent with the target |
| [[LINC02582]] | C | LINC02582 activity raises SLCO1B3-SLCO1B7's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 5.71× lower at baseline in the lines without LINC02582 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; co-absent with the target |
| [[DSG4]] | C | DSG4 activity raises SLCO1B3-SLCO1B7's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 8.50× lower at baseline in the lines without DSG4 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031; co-absent with the target |
| [[POU5F1]] | C | POU5F1 activity raises SLCO1B3-SLCO1B7's level | lines that do not express POU5F1 (27) vs lines expressing it (23) | 2.75× lower at baseline in the lines without POU5F1 | 0.042 | ⚠ within organs, on part of the lines; also absent: P2RY2, C4BPB, UGT1A6; co-absent with the target |
| [[C4BPB]] | C | C4BPB activity raises SLCO1B3-SLCO1B7's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 3.75× lower at baseline in the lines without C4BPB | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4; co-absent with the target |
| [[HNF4A]] | C | HNF4A activity raises SLCO1B3-SLCO1B7's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 3.55× lower at baseline in the lines without HNF4A | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM32]] | B | SLCO1B3-SLCO1B7 activity raises ADAM32's level | lines that do not express SLCO1B3-SLCO1B7 (27) vs lines expressing it (23) | 1.53× lower at baseline in the lines without SLCO1B3-SLCO1B7 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000257062, SLCO1B3, SLCO1B1 |
| [[LINC00707]] | B | SLCO1B3-SLCO1B7 activity raises LINC00707's level | lines that do not express SLCO1B3-SLCO1B7 (27) vs lines expressing it (23) | 2.03× lower at baseline in the lines without SLCO1B3-SLCO1B7 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000257062, SLCO1B3, SLCO1B1 |
| [[LINC02516]] | B | SLCO1B3-SLCO1B7 activity raises LINC02516's level | lines that do not express SLCO1B3-SLCO1B7 (27) vs lines expressing it (23) | 1.71× lower at baseline in the lines without SLCO1B3-SLCO1B7 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000257062, SLCO1B3, SLCO1B1 |
| [[SLCO1B3]] | C | SLCO1B3-SLCO1B7 activity raises SLCO1B3's level | lines that do not express SLCO1B3-SLCO1B7 (27) vs lines expressing it (23) | 11.50× lower at baseline in the lines without SLCO1B3-SLCO1B7 | 8e-06 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000257062, SLCO1B3, SLCO1B1; co-absent with the target |
| [[SLCO1B1]] | C | SLCO1B3-SLCO1B7 activity raises SLCO1B1's level | lines that do not express SLCO1B3-SLCO1B7 (27) vs lines expressing it (23) | 3.89× lower at baseline in the lines without SLCO1B3-SLCO1B7 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000257062, SLCO1B3, SLCO1B1; co-absent with the target |
| [[POU5F1]] | C | SLCO1B3-SLCO1B7 activity raises POU5F1's level | lines that do not express SLCO1B3-SLCO1B7 (27) vs lines expressing it (23) | 2.29× lower at baseline in the lines without SLCO1B3-SLCO1B7 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000257062, SLCO1B3, SLCO1B1; co-absent with the target |
| [[LINC02582]] | C | SLCO1B3-SLCO1B7 activity raises LINC02582's level | lines that do not express SLCO1B3-SLCO1B7 (27) vs lines expressing it (23) | 3.10× lower at baseline in the lines without SLCO1B3-SLCO1B7 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000257062, SLCO1B3, SLCO1B1; co-absent with the target |
| [[TIMD4]] | C | SLCO1B3-SLCO1B7 activity raises TIMD4's level | lines that do not express SLCO1B3-SLCO1B7 (27) vs lines expressing it (23) | 1.43× lower at baseline in the lines without SLCO1B3-SLCO1B7 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000257062, SLCO1B3, SLCO1B1; co-absent with the target |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.586). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.7, 48.3); signed map (67.5, 7.0). **Vector** length 69.1, 21.2% of its response variance represented; |z| ≥ 3 in 480 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +4.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.5 | +0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +2.5 |
| fall | [[Radotinib (drug)]] 5 µM |  | -2.2 | -3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.7 | -6.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.5 | -5.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -1.3 | -3.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | -1.1 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.1 | -0.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | SLCO1B3-SLCO1B7 readthrough |
| Locus type | readthrough (other) |
| Location | 12p12.2 — chr12:20,815,674-21,090,245 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OATP1B3-1B7, LST-3TM12 |
| Matched by | ensembl_id |

**Function**, from UniProt [F5H094](https://www.uniprot.org/uniprotkb/F5H094) (SLCO1B3-SLCO1B7 readthrough transcript protein):

> Mediates the Na(+)-independent uptake of organic anions. Transports the conjugated steroids 17-beta-glucuronosyl estradiol (17beta-estradiol 17-O-(beta-D-glucuronate) or E2G) and dehydroepiandrosterone 3-sulfate (DHEAS) at the smooth endoplasmic reticulum membrane (SER), granting access to metabolizing enzymes. Contributes to the metabolism of bile acids such as taurocholate (cholyltaurine) and lithocholate, by functioning as a doorway between SER and cytosol, thereby decreasing their …

**Summary**, from NCBI Gene [115072896](https://www.ncbi.nlm.nih.gov/gene/115072896):

> This locus represents naturally occurring readthrough transcription between the neighboring SLCO1B3 (solute carrier organic anion transporter family member 1B3) and SLCO1B7 (solute carrier organic anion transporter family member 1B7 (putative)) genes on chromosome 12. The readthrough transcript encodes a protein that shares sequence identity with both the upstream and downstream genes. [provided by RefSeq, Jun 2019]

**Accessions** — [HGNC:54403](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54403) · Entrez [115072896](https://www.ncbi.nlm.nih.gov/gene/115072896) · UniProt [F5H094](https://www.uniprot.org/uniprotkb/F5H094) · Ensembl [ENSG00000257046](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257046)

## Data

Gene col 15018: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15018); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15018, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15018]; `tensor/DDL_lfc|DDL_z.npy` [15018]; `embed/gene_vectors.npy` [15018]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15018 or target_col == 15018). Every well: [[SLCO1B3-SLCO1B7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLCO1B3-SLCO1B7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
