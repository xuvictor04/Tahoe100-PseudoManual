---
symbol: "RHOJ"
type: "gene"
col: 4765
ensembl_id: "ENSG00000126785"
name: "ras homolog family member J"
location: "14q23.2"
module: 87
arm: "+"
pooled_cpm: 7.56
n_lines_expressing: 17
n_dd_up: 4
n_dd_down: 7
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 13
direction_downstream: 30
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# RHOJ

*ras homolog family member J* — 14q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.18× (z +8.5, q 2e-14, up in 0 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.87× (z +6.5, q 2e-08, up in 0 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.538× (z -4.5, q 0.003, down in 12 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C10orf90]] (+0.72, fdr 7e-06), [[COL19A1]] (+0.69, fdr 7e-06), [[SOX10]] (+0.67, fdr 7e-06).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 30 go from it, the strongest it → [[PCDHGA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4765.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.18×** | +8.5 | 2e-14 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.98×** | +7.7 | 5e-12 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +6.5 | 2e-08 | 0/11 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.39×** | +5.9 | 5e-07 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.55× | +3.2 | 0.16 | 0/10 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.88× | +3.1 | 0.16 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 2.25× | +3.1 | 0.16 | 0/7 | rises with dose | noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.05 µM |  | 1.52× | +3.1 | 0.16 | 5/9 (A-172, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4765.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.538×** | -4.5 | 0.003 | 12/13 (Hs 766T, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.556×** | -4.3 | 0.005 | 13/13 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.572×** | -4.1 | 0.008 | 8/12 (LOX-IMVI, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.583×** | -4.0 | 0.011 | 12/14 (Hs 766T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.621×** | -3.5 | 0.048 | 5/13 (LOX-IMVI, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Artesunate (drug)]] 5 µM |  | **0.716×** | -3.5 | 0.048 | 5/14 (HepG2/C3A, SNU-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | **0.618×** | -3.3 | 0.088 | 1/13 (hTERT-HPNE) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.634× | -3.1 | 0.14 | 2/13 (HepG2/C3A, RPMI-7951) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4765. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 189 | 0 | 14 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0747× (z -15.6) |
| [[Hs 766T (line)]] | wt | 91.3 | 0 | 10 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0233× (z -17.8) |
| [[LOX-IMVI (line)]] | wt | 15.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0311× (z -16.2) |
| [[C-33 A (line)]] | alt | 23.4 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0716× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 27.5 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0127× (z -18.8) |
| [[A-172 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.571 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.622 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.686 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.758 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.731 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.732 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.900 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.842 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.958 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.911 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.879 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.820 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.675 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.726 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.705 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.631 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.758 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.793 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.650 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.762 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.769 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.738 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4765), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C10orf90]] | +0.72 | +0.66 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[COL19A1]] | +0.69 | +0.60 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SOX10]] | +0.67 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[LEF1-AS1]] | +0.66 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[LOXL3]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[AEBP1]] | +0.62 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[SAMMSON]] | +0.61 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[CTHRC1]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[LEF1]] | +0.61 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[MIR3681HG]] | +0.61 | +0.59 / +0.57 | both halves | 8e-06 |  |
| [[PAX3]] | +0.60 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[STAG3]] | +0.60 | +0.60 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 1, C 12. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises RHOJ's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LHFPL3-AS1]] | C | LHFPL3-AS1 activity raises RHOJ's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 5.34× lower at baseline in the lines without LHFPL3-AS1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |
| [[CCDC190]] | C | CCDC190 activity raises RHOJ's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 3.15× lower at baseline in the lines without CCDC190 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337; co-absent with the target |
| [[ECSCR]] | C | ECSCR activity raises RHOJ's level | lines that do not express ECSCR (35) vs lines expressing it (15) | 3.36× lower at baseline in the lines without ECSCR | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, ADGRF5, ENSG00000243486; maybe low, not absent; co-absent with the target |
| [[PLPP4]] | C | PLPP4 activity raises RHOJ's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 3.13× lower at baseline in the lines without PLPP4 | 0.050 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6; co-absent with the target |
| [[MEOX2]] | C | MEOX2 activity raises RHOJ's level | lines that do not express MEOX2 (36) vs lines expressing it (14) | 2.67× lower at baseline in the lines without MEOX2 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02566, MMRN1, ENSG00000232252; co-absent with the target |
| [[FN1]] | C | FN1 activity raises RHOJ's level | lines that do not express FN1 (29) vs lines expressing it (21) | 2.72× lower at baseline in the lines without FN1 | 0.064 | ⚠ within organs, on part of the lines; also absent: PLPP4, ENSG00000234261, IL7R; co-absent with the target |
| [[RMEL3]] | C | RMEL3 activity raises RHOJ's level | lines that do not express RMEL3 (26) vs lines expressing it (24) | 2.27× lower at baseline in the lines without RMEL3 | 0.067 | ⚠ within organs, on part of the lines; also absent: LINC00698, COL19A1, AEBP1; maybe low, not absent; co-absent with the target |
| [[TIMP3]] | C | TIMP3 activity raises RHOJ's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 2.57× lower at baseline in the lines without TIMP3 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1; co-absent with the target |
| [[ARHGAP20]] | C | ARHGAP20 activity raises RHOJ's level | lines that do not express ARHGAP20 (34) vs lines expressing it (16) | 2.51× lower at baseline in the lines without ARHGAP20 | 0.070 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, GYPC; co-absent with the target |
| [[FCRLA]] | C | FCRLA activity raises RHOJ's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 3.50× lower at baseline in the lines without FCRLA | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |
| [[SOX10]] | C | SOX10 activity raises RHOJ's level | lines that do not express SOX10 (45) vs lines expressing it (5) | 7.17× lower at baseline in the lines without SOX10 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01425, ENSG00000241168, TYR; co-absent with the target |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 1, C 29. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDHGA2]] | B | RHOJ activity raises PCDHGA2's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 2.41× lower at baseline in the lines without RHOJ | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240 |
| [[LINC02267]] | C | RHOJ activity raises LINC02267's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 2.13× lower at baseline in the lines without RHOJ | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240; co-absent with the target |
| [[FCRLA]] | C | RHOJ activity raises FCRLA's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 2.35× lower at baseline in the lines without RHOJ | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240; co-absent with the target |
| [[TYR]] | C | RHOJ activity raises TYR's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 2.07× lower at baseline in the lines without RHOJ | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240; co-absent with the target |
| [[SOX10]] | C | RHOJ activity raises SOX10's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 2.55× lower at baseline in the lines without RHOJ | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240; co-absent with the target |
| [[LHFPL3-AS1]] | C | RHOJ activity raises LHFPL3-AS1's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 3.09× lower at baseline in the lines without RHOJ | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240; co-absent with the target |
| [[LINC00879]] | C | RHOJ activity raises LINC00879's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 1.28× lower at baseline in the lines without RHOJ | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240; co-absent with the target |
| [[A2M]] | C | RHOJ activity raises A2M's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 4.07× lower at baseline in the lines without RHOJ | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240; co-absent with the target |
| [[TF]] | C | RHOJ activity raises TF's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 2.42× lower at baseline in the lines without RHOJ | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240; co-absent with the target |
| [[LINC02566]] | C | RHOJ activity raises LINC02566's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 1.53× lower at baseline in the lines without RHOJ | 8e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240; co-absent with the target |
| [[LINC02941]] | C | RHOJ activity raises LINC02941's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 2.50× lower at baseline in the lines without RHOJ | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240; co-absent with the target |
| [[C10orf90]] | C | RHOJ activity raises C10orf90's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 2.65× lower at baseline in the lines without RHOJ | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.749). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (52.8, 28.1); signed map (28.6, 39.6). **Vector** length 54.8, 19.1% of its response variance represented; |z| ≥ 3 in 426 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.1 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +5.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.4 | +1.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.4 | +6.5 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.4 | +2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +0.9 | -0.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.9 | +1.2 |
|  | [[EX229 (drug)]] 5 µM |  | +0.8 | +0.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +0.7 | +0.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +0.7 | +1.0 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.4 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.1 | -3.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.1 | -1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.1 | -0.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -0.9 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -0.9 | +1.0 |

## What is on record

|  |  |
|---|---|
| Name | ras homolog family member J |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.2 — chr14:63,204,114-63,293,508 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14445, TCL; previously RASL7B, ARHJ |
| Gene groups (HGNC) | Rho family GTPases |
| Reactome | 4 pathways, smallest: RHOJ GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4E5](https://www.uniprot.org/uniprotkb/Q9H4E5) (Rho-related GTP-binding protein RhoJ):

> Plasma membrane-associated small GTPase specifically involved in angiogenesis. Required for endothelial cell migration during vascular development via its interaction with GLUL. Elicits the formation of F-actin-rich structures, thereby regulating endothelial cell migration.

**Summary**, from NCBI Gene [57381](https://www.ncbi.nlm.nih.gov/gene/57381):

> This gene encodes one of the many small GTP-binding proteins in the Rho family shown to be associated with focal adhesions in endothelial cells (PMID: 21148427, 22103495). The encoded protein is activated by vascular endothelial growth factor and may regulate angiogenesis. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:688](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:688) · Entrez [57381](https://www.ncbi.nlm.nih.gov/gene/57381) · UniProt [Q9H4E5](https://www.uniprot.org/uniprotkb/Q9H4E5) · Ensembl [ENSG00000126785](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126785)

## Data

Gene col 4765: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4765); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4765, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4765]; `tensor/DDL_lfc|DDL_z.npy` [4765]; `embed/gene_vectors.npy` [4765]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4765 or target_col == 4765). Every well: [[RHOJ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHOJ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
