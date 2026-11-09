---
symbol: "SSX1"
type: "gene"
col: 4757
ensembl_id: "ENSG00000126752"
name: "SSX family member 1"
location: "Xp11.23"
module: 72
arm: "+"
pooled_cpm: 2.14
n_lines_expressing: 7
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 9
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# SSX1

*SSX family member 1* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 9.97× (z +9.9, q 2e-20, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 2.40× (z +5.6, q 4e-06, up in 0 of 5 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[(S)-Crizotinib (drug)]] 0.05 µM: 0.407× (z -3.8, q 0.086, down in 0 of 5 measured lines).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BHMT2]] (+0.63, fdr 3e-05), [[DYNC1I1]] (+0.58, fdr 6e-05), [[GUCY1B1]] (+0.57, fdr 8e-05); moves opposite to [[KPNB1-DT]] (-0.41, fdr 8e-04, ⚠ not reproduced), [[DCAF10]] (-0.40, fdr 3e-04).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SRRM4]] → it (grade C ⚠); 9 go from it, the strongest it → [[MAP1A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4757.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **9.97×** | +9.9 | 2e-20 | 1/2 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **8.26×** | +9.5 | 6e-19 | 2/3 (SK-MEL-2, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.02×** | +6.7 | 4e-09 | 1/3 (SK-MEL-2) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.40×** | +5.6 | 4e-06 | 0/5 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **3.24×** | +5.3 | 1e-05 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **5.87×** | +4.6 | 5e-04 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.70×** | +4.3 | 0.001 | 1/4 (SNU-1) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **2.57×** | +4.2 | 0.001 | 0/4 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.66×** | +4.2 | 0.001 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.90×** | +3.7 | 0.011 | 2/3 (HS-578T, SK-MEL-2) | top dose only | noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | **1.77×** | +3.6 | 0.014 | 0/4 | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.31×** | +3.6 | 0.014 | 3/4 (SK-MEL-2, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +3.6 | 0.014 | 0/4 | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +3.4 | 0.032 | 0/5 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.11×** | +3.3 | 0.032 | 3/5 (SNU-1, hTERT-HPNE, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.18×** | +3.3 | 0.034 | 3/5 (SHP-77, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cinacalcet (drug)]] 0.5 µM |  | **1.97×** | +3.0 | 0.072 | 0/5 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4757.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | **0.407×** | -3.8 | 0.086 | 0/5 | inconsistent across doses | position effect removed |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.436×** | -3.6 | 0.086 | 0/5 | top dose only | plate-row cell shift |
| [[Cloxacillin (sodium) (drug)]] 0.5 µM |  | 0.466× | -3.4 | 0.11 | 0/5 | inconsistent across doses |  |
| [[Dabrafenib (drug)]] 5 µM |  | 0.279× | -3.0 | 0.37 | 0/5 | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4757. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 0.185 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.145 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.163 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.142 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.422 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.193 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.152 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.210 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.367 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.172 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.229 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.192 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.226 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.193 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.216 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.183 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.208 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.199 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.208 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.186 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.164 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.216 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.168 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.165 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.200 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.163 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.143 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.154 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.134 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.193 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.206 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.158 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.164 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.183 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.395 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.378 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.229 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.188 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.244 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.182 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4757), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 15 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BHMT2]] | +0.63 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[DYNC1I1]] | +0.58 | +0.54 / +0.38 | both halves | 6e-05 |  |
| [[GUCY1B1]] | +0.57 | +0.42 / +0.37 | both halves | 8e-05 |  |
| [[TDO2]] | +0.56 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[MAP1A]] | +0.54 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[B4GALNT1]] | +0.53 | +0.50 / +0.38 | both halves | 6e-05 |  |
| [[NSFL1C]] | +0.53 | +0.51 / +0.35 | both halves | 1e-04 |  |
| [[PDGFD]] | +0.53 | +0.40 / +0.32 | both halves | 1e-04 |  |
| [[EGF]] | +0.51 | +0.34 / +0.49 | both halves | 1e-04 |  |
| [[PLAA]] | +0.51 | +0.54 / +0.32 | both halves | 2e-04 |  |
| [[AP4B1]] | +0.50 | +0.45 / +0.29 | both halves | 2e-04 |  |
| [[DGKG]] | +0.49 | +0.42 / +0.26 | both halves | 4e-04 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNB1-DT]] | -0.41 | -0.40 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[DCAF10]] | -0.40 | -0.29 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRRM4]] | C | SRRM4 activity raises SSX1's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 2.34× lower at baseline in the lines without SRRM4 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises SSX1's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 2.03× lower at baseline in the lines without RIT2 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises SSX1's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 2.03× lower at baseline in the lines without SYT4 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[CDH6]] | C | CDH6 activity raises SSX1's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 1.40× lower at baseline in the lines without CDH6 | 0.080 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC; co-absent with the target |
| [[LINC01287]] | C | LINC01287 activity raises SSX1's level | lines that do not express LINC01287 (39) vs lines expressing it (11) | 2.68× lower at baseline in the lines without LINC01287 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253642, POU6F2, RIT2; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP1A]] | B | SSX1 activity raises MAP1A's level | lines that do not express SSX1 (43) vs lines expressing it (7) | 2.30× lower at baseline in the lines without SSX1 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00879, LINC02099, RNF17 |
| [[RIT2]] | C | SSX1 activity raises RIT2's level | lines that do not express SSX1 (43) vs lines expressing it (7) | 3.78× lower at baseline in the lines without SSX1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00879, LINC02099, RNF17; co-absent with the target |
| [[SYT4]] | C | SSX1 activity raises SYT4's level | lines that do not express SSX1 (43) vs lines expressing it (7) | 3.55× lower at baseline in the lines without SSX1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00879, LINC02099, RNF17; co-absent with the target |
| [[LRFN2]] | C | SSX1 activity raises LRFN2's level | lines that do not express SSX1 (43) vs lines expressing it (7) | 3.15× lower at baseline in the lines without SSX1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00879, LINC02099, RNF17; co-absent with the target |
| [[SRRM4]] | C | SSX1 activity raises SRRM4's level | lines that do not express SSX1 (43) vs lines expressing it (7) | 2.77× lower at baseline in the lines without SSX1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00879, LINC02099, RNF17; co-absent with the target |
| [[LINC01287]] | C | SSX1 activity raises LINC01287's level | lines that do not express SSX1 (43) vs lines expressing it (7) | 4.10× lower at baseline in the lines without SSX1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00879, LINC02099, RNF17; co-absent with the target |
| [[KCNE4]] | C | SSX1 activity raises KCNE4's level | lines that do not express SSX1 (43) vs lines expressing it (7) | 5.09× lower at baseline in the lines without SSX1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00879, LINC02099, RNF17; co-absent with the target |
| [[KHDRBS2]] | C | SSX1 activity raises KHDRBS2's level | lines that do not express SSX1 (43) vs lines expressing it (7) | 2.72× lower at baseline in the lines without SSX1 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00879, LINC02099, RNF17; co-absent with the target |
| [[JAM3]] | C | SSX1 activity raises JAM3's level | lines that do not express SSX1 (43) vs lines expressing it (7) | 4.15× lower at baseline in the lines without SSX1 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00879, LINC02099, RNF17; co-absent with the target |

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.445). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.8, 50.5); signed map (51.8, -13.8). **Vector** length 8.62, 1.71% of its response variance represented; |z| ≥ 3 in 91 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.0 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +0.9 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.8 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.8 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.7 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.6 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.4 | +1.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +0.3 | +0.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.4 | -1.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.3 | -0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.3 | -1.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.3 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.2 | -0.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.2 | -1.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -0.2 | -0.2 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.2 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | SSX family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:48,255,392-48,267,444 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CT5.1 |
| Gene groups (HGNC) | SSX family; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16384](https://www.uniprot.org/uniprotkb/Q16384) (Protein SSX1):

> Could act as a modulator of transcription. Plays a role in spermatogenesis.

**Summary**, from NCBI Gene [6756](https://www.ncbi.nlm.nih.gov/gene/6756):

> The product of this gene belongs to the family of highly homologous synovial sarcoma X (SSX) breakpoint proteins. These proteins may function as transcriptional repressors. They are also capable of eliciting spontaneous humoral and cellular immune responses in cancer patients, and are potentially useful targets in cancer vaccine-based immunotherapy. This gene, and also the SSX2 and SSX4 family members, have been involved in t(X;18)(p11.2;q11.2) translocations that are characteristically found …

**Accessions** — [HGNC:11335](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11335) · Entrez [6756](https://www.ncbi.nlm.nih.gov/gene/6756) · UniProt [Q16384](https://www.uniprot.org/uniprotkb/Q16384) · Ensembl [ENSG00000126752](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126752)

## Data

Gene col 4757: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4757); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4757, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4757]; `tensor/DDL_lfc|DDL_z.npy` [4757]; `embed/gene_vectors.npy` [4757]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4757 or target_col == 4757). Every well: [[SSX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SSX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
