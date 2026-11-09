---
symbol: "PALMD"
type: "gene"
col: 1788
ensembl_id: "ENSG00000099260"
name: "palmdelphin"
location: "1p21.2"
module: 19
arm: "+"
pooled_cpm: 2.7
n_lines_expressing: 23
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 8
direction_downstream: 10
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# PALMD

*palmdelphin* — 1p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.40× (z +11.3, q 9e-27, up in 1 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.61× (z +4.6, q 4e-04, up in 1 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Dihydroartemisinin (drug)]] 5 µM: 0.555× (z -4.1, q 0.020, down in 5 of 17 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (CFPAC-1 0.114×, NCI-H460 0.149×, BT-474 0.0969×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H460 0.0163×, CFPAC-1 0.0722×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 0.168×, CFPAC-1 0.258×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0556×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDE7B]] (+0.67, fdr 7e-06), [[COL4A6]] (+0.65, fdr 7e-06), [[SERPINB11]] (+0.63, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[SPP1]] → it (grade C ⚠); 10 go from it, the strongest it → [[KCNMB2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1788.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.40×** | +11.3 | 9e-27 | 1/5 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.70×** | +9.1 | 3e-17 | 2/8 (NCI-H2030, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.98×** | +6.8 | 2e-09 | 1/5 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +5.1 | 4e-05 | 2/10 (NCI-H23, A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +4.6 | 4e-04 | 1/16 (A549) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.83×** | +4.2 | 0.003 | 1/9 (HepG2/C3A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +4.0 | 0.005 | 0/7 | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.17×** | +3.8 | 0.009 | 1/5 (Hs 766T) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.69×** | +3.5 | 0.029 | 6/16 (NCI-H2030, Hs 766T, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.50×** | +3.3 | 0.049 | 0/4 | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +3.3 | 0.051 | 0/11 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.57×** | +3.1 | 0.091 | 1/13 (A-172) | top dose only | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 0.5 µM |  | **1.86×** | +3.1 | 0.091 | 0/13 | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1788.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (CFPAC-1 0.114×, NCI-H460 0.149×, BT-474 0.0969×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H460 0.0163×, CFPAC-1 0.0722×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 0.168×, CFPAC-1 0.258×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0556×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.555×** | -4.1 | 0.020 | 5/17 (A549, A498, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.626× | -3.3 | 0.27 | 2/17 (BT-474, KATO III) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.630× | -3.1 | 0.32 | 4/18 (NCI-H1792, NCI-H460, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1788. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.4 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0163× (z -19.2) |
| [[CFPAC-1 (line)]] | alt | 20.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -15.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0722× (z -13.2) |
| [[BT-474 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0969× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.290 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.796 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.732 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.484 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.522 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.654 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.387 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.439 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.393 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.875 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.321 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.334 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.422 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.416 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.969 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.511 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.359 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.893 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.399 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.419 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.367 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1788), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE7B]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[COL4A6]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[SERPINB11]] | +0.63 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[LINC01035]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[PAX7]] | +0.61 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[GPRIN3]] | +0.60 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[PDE1A]] | +0.59 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[COL4A5]] | +0.59 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[GREM2]] | +0.59 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[RHOH]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[NOVA1]] | +0.58 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[LIN7A]] | +0.58 | +0.43 / +0.63 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPP1]] | C | SPP1 activity raises PALMD's level | lines that do not express SPP1 (35) vs lines expressing it (15) | 2.02× lower at baseline in the lines without SPP1 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01320, MAGEB2, FGG; co-absent with the target |
| [[KCNJ6]] | C | KCNJ6 activity raises PALMD's level | lines that do not express KCNJ6 (23) vs lines expressing it (27) | 1.96× lower at baseline in the lines without KCNJ6 | 0.043 | ⚠ within organs, on part of the lines; also absent: LRP2, ENTHD1, MLLT11; maybe low, not absent; co-absent with the target |
| [[FGB]] | C | FGB activity raises PALMD's level | lines that do not express FGB (42) vs lines expressing it (8) | 2.67× lower at baseline in the lines without FGB | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2; co-absent with the target |
| [[SERPINB11]] | C | SERPINB11 activity raises PALMD's level | lines that do not express SERPINB11 (43) vs lines expressing it (7) | 2.96× lower at baseline in the lines without SERPINB11 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SUCNR1, HOPX; co-absent with the target |
| [[NOVA1]] | C | NOVA1 activity raises PALMD's level | lines that do not express NOVA1 (27) vs lines expressing it (23) | 2.02× lower at baseline in the lines without NOVA1 | 0.064 | ⚠ within organs, on part of the lines; also absent: EPHA6, ZYG11A, GALNT13; co-absent with the target |
| [[FGG]] | C | FGG activity raises PALMD's level | lines that do not express FGG (42) vs lines expressing it (8) | 3.19× lower at baseline in the lines without FGG | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB; co-absent with the target |
| [[GPRIN3]] | C | GPRIN3 activity raises PALMD's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 1.56× lower at baseline in the lines without GPRIN3 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031; co-absent with the target |
| [[FGA]] | C | FGA activity raises PALMD's level | lines that do not express FGA (43) vs lines expressing it (7) | 2.26× lower at baseline in the lines without FGA | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 5, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNMB2]] | B | PALMD activity raises KCNMB2's level | lines that do not express PALMD (27) vs lines expressing it (23) | 2.11× lower at baseline in the lines without PALMD | 0.049 | ⚠ within organs, on part of the lines; also absent: GPRC5B, FAM110B, SHISAL1; maybe low, not absent |
| [[WDR72]] | B | PALMD activity raises WDR72's level | lines that do not express PALMD (27) vs lines expressing it (23) | 1.62× lower at baseline in the lines without PALMD | 0.077 | ⚠ within organs, on part of the lines; also absent: GPRC5B, FAM110B, SHISAL1; maybe low, not absent |
| [[NRG4]] | B | PALMD activity raises NRG4's level | lines that do not express PALMD (27) vs lines expressing it (23) | 1.89× lower at baseline in the lines without PALMD | 0.089 | ⚠ within organs, on part of the lines; also absent: GPRC5B, FAM110B, SHISAL1; maybe low, not absent |
| [[MEIS1]] | B | PALMD activity raises MEIS1's level | lines that do not express PALMD (27) vs lines expressing it (23) | 2.57× lower at baseline in the lines without PALMD | 0.094 | ⚠ within organs, on part of the lines; also absent: GPRC5B, FAM110B, SHISAL1; maybe low, not absent |
| [[PDE1C]] | B | PALMD activity raises PDE1C's level | lines that do not express PALMD (27) vs lines expressing it (23) | 2.06× lower at baseline in the lines without PALMD | 0.099 | ⚠ within organs, on part of the lines; also absent: GPRC5B, FAM110B, SHISAL1; maybe low, not absent |
| [[NEFL]] | C | PALMD activity raises NEFL's level | lines that do not express PALMD (27) vs lines expressing it (23) | 3.18× lower at baseline in the lines without PALMD | 0.037 | ⚠ within organs, on part of the lines; also absent: GPRC5B, FAM110B, SHISAL1; maybe low, not absent; co-absent with the target |
| [[NCKAP5]] | C | PALMD activity raises NCKAP5's level | lines that do not express PALMD (27) vs lines expressing it (23) | 2.60× lower at baseline in the lines without PALMD | 0.051 | ⚠ within organs, on part of the lines; also absent: GPRC5B, FAM110B, SHISAL1; maybe low, not absent; co-absent with the target |
| [[LGSN]] | C | PALMD activity raises LGSN's level | lines that do not express PALMD (27) vs lines expressing it (23) | 2.29× lower at baseline in the lines without PALMD | 0.079 | ⚠ within organs, on part of the lines; also absent: GPRC5B, FAM110B, SHISAL1; maybe low, not absent; co-absent with the target |
| [[GSDMC]] | C | PALMD activity raises GSDMC's level | lines that do not express PALMD (27) vs lines expressing it (23) | 1.78× lower at baseline in the lines without PALMD | 0.082 | ⚠ within organs, on part of the lines; also absent: GPRC5B, FAM110B, SHISAL1; maybe low, not absent; co-absent with the target |
| [[LINC01967]] | C | PALMD activity raises LINC01967's level | lines that do not express PALMD (27) vs lines expressing it (23) | 1.41× lower at baseline in the lines without PALMD | 0.089 | ⚠ within organs, on part of the lines; also absent: GPRC5B, FAM110B, SHISAL1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.682). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.8, 36.6); signed map (44.3, 43.4). **Vector** length 43.1, 10.7% of its response variance represented; |z| ≥ 3 in 462 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +0.7 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.1 | +1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.1 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.0 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -3.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.5 | -2.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -3.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.4 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | palmdelphin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.2 — chr1:99,646,113-99,694,541 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20271, PALML; previously C1orf11 |
| Gene groups (HGNC) | Paralemmins |
| Matched by | ensembl_id |

UniProt [Q9NP74](https://www.uniprot.org/uniprotkb/Q9NP74) carries no function annotation.

**Summary**, from NCBI Gene [54873](https://www.ncbi.nlm.nih.gov/gene/54873):

> Predicted to be involved in regulation of cell shape. Located in actin cytoskeleton. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15846](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15846) · Entrez [54873](https://www.ncbi.nlm.nih.gov/gene/54873) · UniProt [Q9NP74](https://www.uniprot.org/uniprotkb/Q9NP74) · Ensembl [ENSG00000099260](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099260)

## Data

Gene col 1788: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1788); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1788, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1788]; `tensor/DDL_lfc|DDL_z.npy` [1788]; `embed/gene_vectors.npy` [1788]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1788 or target_col == 1788). Every well: [[PALMD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PALMD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
