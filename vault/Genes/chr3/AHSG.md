---
symbol: "AHSG"
type: "gene"
col: 6962
ensembl_id: "ENSG00000145192"
name: "alpha 2-HS glycoprotein"
location: "3q27.3"
module: 8
arm: "+"
pooled_cpm: 9.0
n_lines_expressing: 5
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# AHSG

*alpha 2-HS glycoprotein* — 3q27.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 9.70× (z +11.1, q 6e-26, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.78× (z +10.8, q 8e-25, up in 1 of 1 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.250×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.176×).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALB]] (+0.92, fdr 7e-06), [[APOA1]] (+0.71, fdr 7e-06), [[AFP]] (+0.69, fdr 7e-06); moves opposite to [[MRPS16]] (-0.50, fdr 3e-04), [[RFFL]] (-0.45, fdr 0.001, ⚠ not reproduced), [[SLC35A4]] (-0.44, fdr 2e-04), [[GLRX2]] (-0.42, fdr 4e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SERPINF1]] → it (grade C ⚠); 6 go from it, the strongest it → [[MIS18A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6962.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **9.70×** | +11.1 | 6e-26 | 1/1 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.78×** | +10.8 | 8e-25 | 1/1 (HepG2/C3A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.65×** | +10.2 | 6e-22 | 1/1 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.66×** | +6.3 | 3e-08 | 1/1 (HepG2/C3A) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.83×** | +6.1 | 2e-07 | 1/1 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.01×** | +5.2 | 2e-05 | 1/1 (HepG2/C3A) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **6.14×** | +4.6 | 3e-04 | 1/1 (HepG2/C3A) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **2.38×** | +4.2 | 0.002 | 0/1 | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.08×** | +3.6 | 0.023 | 0/1 | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **2.01×** | +3.4 | 0.040 | 0/1 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.99×** | +3.3 | 0.042 | 1/2 (HepG2/C3A) | rises with dose | composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.97×** | +3.3 | 0.045 | 0/1 | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +3.2 | 0.064 | 0/2 | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.88×** | +3.1 | 0.083 | 0/1 | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.250×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.176×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6962. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 706 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -11.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -9.9) |
| [[A-172 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.960 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.838 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.884 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.880 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.955 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.982 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.937 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.825 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.847 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.937 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.996 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.784 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.894 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.766 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.927 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.990 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6962), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 14 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALB]] | +0.92 | +0.95 / +0.93 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation; STRING 999 |
| [[APOA1]] | +0.71 | +0.77 / +0.86 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation; STRING 944 |
| [[AFP]] | +0.69 | +0.87 / +0.83 | both halves | 7e-06 | pathway: Post-translational protein phosphorylation; STRING 920 |
| [[AMBP]] | +0.67 | +0.76 / +0.60 | both halves | 7e-06 | STRING 932 |
| [[APOH]] | +0.57 | +0.66 / +0.74 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation; STRING 957 |
| [[PIGR]] | +0.54 | +0.27 / +0.29 | both halves | 3e-04 |  |
| [[YBX1]] | +0.54 | +0.17 / +0.45 | ⚠ not reproduced | 0.001 |  |
| [[RPS2]] | +0.54 | +0.38 / +0.36 | both halves | 9e-05 |  |
| [[RPS4X]] | +0.51 | +0.33 / +0.44 | both halves | 1e-04 |  |
| [[BTF3]] | +0.51 | +0.28 / +0.46 | both halves | 3e-04 |  |
| [[RPS20]] | +0.50 | +0.37 / +0.36 | both halves | 1e-04 |  |
| [[PABPC1]] | +0.50 | +0.33 / +0.34 | both halves | 1e-04 |  |
| [[RPL7]] | +0.48 | +0.33 / +0.41 | both halves | 1e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS16]] | -0.50 | -0.34 / -0.28 | both halves | 3e-04 |  |
| [[RFFL]] | -0.45 | -0.37 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[SLC35A4]] | -0.44 | -0.31 / -0.29 | both halves | 2e-04 |  |
| [[GLRX2]] | -0.42 | -0.39 / -0.25 | both halves | 4e-04 |  |
| [[INO80E]] | -0.42 | -0.40 / -0.26 | both halves | 4e-04 |  |
| [[MRPL47]] | -0.41 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[C10orf88]] | -0.41 | -0.38 / -0.28 | both halves | 3e-04 |  |
| [[VPS29]] | -0.40 | -0.35 / -0.23 | both halves | 5e-04 |  |
| [[NME6]] | -0.40 | -0.41 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[CCDC137]] | -0.40 | -0.48 / -0.13 | ⚠ not reproduced | 0.002 |  |
| [[MIS18A]] | -0.40 | -0.38 / -0.22 | both halves | 6e-04 |  |
| [[CFAP298]] | -0.40 | -0.23 / -0.21 | both halves | 6e-04 |  |
| [[TCHP]] | -0.40 | -0.31 / -0.24 | both halves | 4e-04 |  |
| [[MRPL58]] | -0.40 | -0.38 / -0.27 | both halves | 3e-04 |  |
| [[PSMD3]] | -0.40 | -0.31 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINF1]] | C | SERPINF1 activity raises AHSG's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.71× lower at baseline in the lines without SERPINF1 | 0.053 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent; co-absent with the target |
| [[APOA2]] | C | APOA2 activity raises AHSG's level | lines that do not express APOA2 (46) vs lines expressing it (4) | 13.22× lower at baseline in the lines without APOA2 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, AFP, BMP10; co-absent with the target; its own permutation p |
| [[BMP10]] | C | BMP10 activity raises AHSG's level | lines that do not express BMP10 (47) vs lines expressing it (3) | 3.51× lower at baseline in the lines without BMP10 | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC02099, APOB, TBXT; co-absent with the target; its own permutation p |
| [[MUC6]] | C | MUC6 activity raises AHSG's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 1.82× lower at baseline in the lines without MUC6 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIS18A]] | B | AHSG, [[ALB]] activity lowers MIS18A's level | lines that do not express AHSG, ALB (45) vs lines expressing them (5) | 1.27× higher at baseline in the lines without AHSG, ALB | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent genes |
| [[BMP10]] | C | AHSG activity raises BMP10's level | lines that do not express AHSG (45) vs lines expressing it (5) | 1.56× lower at baseline in the lines without AHSG | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target |
| [[MUC6]] | C | AHSG activity raises MUC6's level | lines that do not express AHSG (45) vs lines expressing it (5) | 2.14× lower at baseline in the lines without AHSG | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target |
| [[AZGP1]] | C | [[AFP]], AHSG, [[ALB]] activity raises AZGP1's level | lines that do not express AFP, AHSG, ALB (45) vs lines expressing them (5) | 2.62× lower at baseline in the lines without AFP, AHSG, ALB | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target; co-absent genes |
| [[LYZ]] | C | [[AFP]], AHSG, [[ALB]] activity raises LYZ's level | lines that do not express AFP, AHSG, ALB (45) vs lines expressing them (5) | 3.22× lower at baseline in the lines without AFP, AHSG, ALB | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target; co-absent genes |
| [[APOA2]] | C | [[AFP]], AHSG, [[ALB]] activity raises APOA2's level | lines that do not express AFP, AHSG, ALB (45) vs lines expressing them (5) | 7.34× lower at baseline in the lines without AFP, AHSG, ALB | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target; co-absent genes |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.193). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.4, 55.0); signed map (66.7, 20.0). **Vector** length 4.36, 1.57% of its response variance represented; |z| ≥ 3 in 17 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +0.4 | +10.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.3 | +0.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.3 | +0.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.2 | +10.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +0.2 | +3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.1 | -0.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.1 | +0.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.1 | +0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.1 | +0.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.3 | -0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.2 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.2 | -0.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -0.2 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -0.2 | -2.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.1 | -0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | -0.1 | +0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | alpha 2-HS glycoprotein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.3 — chr3:186,613,060-186,621,318 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FETUA, A2HS, HSGA |
| Gene groups (HGNC) | Cystatins, type 4 |
| Reactome | 8 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs); Platelet degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P02765](https://www.uniprot.org/uniprotkb/P02765) (Alpha-2-HS-glycoprotein):

> Promotes endocytosis, possesses opsonic properties and influences the mineral phase of bone. Shows affinity for calcium and barium ions.

**Summary**, from NCBI Gene [197](https://www.ncbi.nlm.nih.gov/gene/197):

> The protein encoded by this gene is a negatively-charged serum glycoprotein that is synthesized by hepatocytes. The encoded protein consists of two polypeptide chains, which are both cleaved from a proprotein encoded from a single mRNA. It is involved in several processes, including endocytosis, brain development, and the formation of bone tissue. Defects in this gene are a cause of susceptibility to leanness. [provided by RefSeq, Aug 2017]

**Accessions** — [HGNC:349](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:349) · Entrez [197](https://www.ncbi.nlm.nih.gov/gene/197) · UniProt [P02765](https://www.uniprot.org/uniprotkb/P02765) · Ensembl [ENSG00000145192](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145192)

## Data

Gene col 6962: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6962); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6962, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6962]; `tensor/DDL_lfc|DDL_z.npy` [6962]; `embed/gene_vectors.npy` [6962]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6962 or target_col == 6962). Every well: [[AHSG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AHSG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
