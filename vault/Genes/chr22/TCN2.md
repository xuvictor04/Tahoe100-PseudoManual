---
symbol: "TCN2"
type: "gene"
col: 11662
ensembl_id: "ENSG00000185339"
name: "transcobalamin 2"
location: "22q12.2"
module: 191
arm: "+"
pooled_cpm: 2.46
n_lines_expressing: 38
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/191"]
generated_by: "tahoemap"
---

# TCN2

*transcobalamin 2* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 31.1× (z +32.3, q 0e+00, up in 26 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Peretinoin (drug)]] 0.5 µM in 1 line (A549 0.0487×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHRS2]] (+0.60, fdr 1e-05), [[CEACAM22P-1]] (+0.60, fdr 1e-05), [[COL26A1]] (+0.57, fdr 7e-06); moves opposite to [[MCM9]] (-0.52, fdr 5e-05), [[SPOPL-DT]] (-0.52, fdr 4e-04), [[TMEM11-DT]] (-0.50, fdr 4e-05).
> It is in [[Module 191]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SRRM3]] → it (grade B ⚠); 3 go from it, the strongest it → [[NAF1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11662.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **31.1×** | +32.3 | 0e+00 | 26/30 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **18.7×** | +27.5 | 0e+00 | 28/30 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **9.12×** | +20.8 | 0e+00 | 23/30 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.02×** | +18.5 | 0e+00 | 16/25 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.91×** | +12.3 | 7e-33 | 2/4 (A498, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.35×** | +10.9 | 1e-25 | 17/28 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +10.7 | 7e-25 | 20/25 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.01×** | +10.3 | 3e-23 | 12/14 (SW 900, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.95×** | +8.9 | 5e-17 | 15/30 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.52×** | +8.0 | 6e-14 | 3/4 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.24×** | +7.6 | 2e-12 | 13/30 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.09×** | +6.9 | 2e-10 | 13/25 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.92×** | +6.1 | 3e-08 | 14/32 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +5.2 | 9e-06 | 8/27 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.60×** | +4.4 | 4e-04 | 8/29 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +4.4 | 4e-04 | 6/28 (HEC-1-A, hTERT-HPNE, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +4.2 | 8e-04 | 6/30 (SW480, C32, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.006 | 8/31 (COLO 205, KATO III, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11662.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Peretinoin (drug)]] 0.5 µM in 1 line (A549 0.0487×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.682× | -3.6 | 0.17 | 7/28 (COLO 205, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.779× | -3.3 | 0.17 | 4/30 (SNU-423, A-172, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.703× | -3.3 | 0.17 | 8/32 (A549, NCI-H1792, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.792× | -3.1 | 0.22 | 6/30 (NCI-H2347, KATO III, …) | top dose only |  |
| [[Tadalafil (drug)]] 5 µM |  | 0.711× | -3.1 | 0.22 | 8/26 (HT-29, SW1417, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.710× | -3.1 | 0.22 | 4/28 (Hs 766T, CFPAC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11662. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 2.60 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 358× (z +17.0) | — |
| [[A549 (line)]] | wt | 3.55 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 71.5× (z +13.4) | [[Peretinoin (drug)]] 0.5 µM 0.0487× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 3.88 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 24.1× (z +11.9) | — |
| [[PANC-1 (line)]] | alt | 0.985 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.8× (z +12.8) | — |
| [[A498 (line)]] | wt | 3.48 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 19.0× (z +12.2) | — |
| [[Hs 766T (line)]] | wt | 2.82 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 59.8× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 1.67 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 90.5× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 3.16 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 35.8× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 3.16 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 90.3× (z +10.6) | — |
| [[KATO III (line)]] | alt | 1.07 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 179× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 1.06 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 164× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 3.39 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 31.1× (z +10.4) | — |
| [[SW1417 (line)]] | alt | 2.38 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 57.1× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 1.09 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 31.9× (z +9.7) | — |
| [[A-172 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.258 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.623 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.994 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.476 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.442 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.279 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.495 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.653 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.254 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.516 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.433 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.274 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11662), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHRS2]] | +0.60 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[CEACAM22P-1]] | +0.60 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[COL26A1]] | +0.57 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[C3]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[RASSF4]] | +0.54 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[RING1]] | +0.54 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[GPR108]] | +0.52 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[VAV1]] | +0.52 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[DNAH3]] | +0.52 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[VASN]] | +0.52 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[LINC00624]] | +0.52 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[PPL]] | +0.51 | +0.41 / +0.45 | both halves | 4e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM9]] | -0.52 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[SPOPL-DT]] | -0.52 | -0.25 / -0.53 | both halves | 4e-04 |  |
| [[TMEM11-DT]] | -0.50 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[MSANTD2]] | -0.49 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[PRKACB]] | -0.47 | -0.32 / -0.28 | both halves | 3e-04 |  |
| [[NAF1]] | -0.47 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[GLUD1P3]] | -0.47 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[MFSD14CP-1]] | -0.47 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[EPM2A]] | -0.47 | -0.25 / -0.45 | both halves | 4e-04 | pathway: Diseases of metabolism |
| [[TRNT1]] | -0.47 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[FBXO22]] | -0.46 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[PBX3]] | -0.46 | -0.39 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRRM3]] | B | SRRM3 activity lowers TCN2's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 1.51× higher at baseline in the lines without SRRM3 | 0.060 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent |
| [[TNFSF14]] | B | TNFSF14 activity raises TCN2's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 1.58× lower at baseline in the lines without TNFSF14 | 0.061 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |
| [[C3]] | B | C3 activity raises TCN2's level | lines that do not express C3 (32) vs lines expressing it (18) | 1.48× lower at baseline in the lines without C3 | 0.077 | ⚠ within organs, on part of the lines; also absent: TNFSF14, CP, CARD11 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NAF1]] | B | TCN2 activity lowers NAF1's level | lines that do not express TCN2 (12) vs lines expressing it (38) | 1.35× higher at baseline in the lines without TCN2 | 0.032 | ⚠ within organs, on part of the lines; also absent: PRSS23, TMSB4X, ARHGAP23; maybe low, not absent |
| [[TIMM23B-AGAP6]] | B | TCN2 activity lowers TIMM23B-AGAP6's level | lines that do not express TCN2 (12) vs lines expressing it (38) | 1.33× higher at baseline in the lines without TCN2 | 0.057 | ⚠ within organs, on part of the lines; also absent: PRSS23, TMSB4X, ARHGAP23; maybe low, not absent |
| [[METTL8]] | B | TCN2 activity lowers METTL8's level | lines that do not express TCN2 (12) vs lines expressing it (38) | 1.53× higher at baseline in the lines without TCN2 | 0.092 | ⚠ within organs, on part of the lines; also absent: PRSS23, TMSB4X, ARHGAP23; maybe low, not absent |

## Where it sits

- **Module**: [[Module 191]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.611). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.6, 34.5); signed map (26.1, 16.4). **Vector** length 43.4, 6.44% of its response variance represented; |z| ≥ 3 in 728 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +10.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.2 | +27.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.2 | +32.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +18.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +8.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.0 | +4.4 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +0.8 | +1.8 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | +0.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.1 | -0.7 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.0 | +0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.8 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | transcobalamin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:30,607,003-30,627,271 (+) |
| Ensembl biotype | protein_coding |
| Also known as | D22S676, D22S750, TC2 |
| Hallmark sets | P53_PATHWAY |
| Reactome | 7 pathways, smallest: Transport of RCbl within the body; Defects in cobalamin (B12) metabolism; Cobalamin (Cbl, vitamin B12) transport and metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P20062](https://www.uniprot.org/uniprotkb/P20062) (Transcobalamin-2):

> Primary vitamin B12-binding and transport protein. Delivers cobalamin to cells.

**Summary**, from NCBI Gene [6948](https://www.ncbi.nlm.nih.gov/gene/6948):

> This gene encodes a member of the vitamin B12-binding protein family. This family of proteins, alternatively referred to as R binders, is expressed in various tissues and secretions. This plasma protein binds cobalamin and mediates the transport of cobalamin into cells. This protein and other mammalian cobalamin-binding proteins, such as transcobalamin I and gastric intrisic factor, may have evolved by duplication of a common ancestral gene. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:11653](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11653) · Entrez [6948](https://www.ncbi.nlm.nih.gov/gene/6948) · UniProt [P20062](https://www.uniprot.org/uniprotkb/P20062) · Ensembl [ENSG00000185339](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185339)

## Data

Gene col 11662: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11662); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11662, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11662]; `tensor/DDL_lfc|DDL_z.npy` [11662]; `embed/gene_vectors.npy` [11662]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11662 or target_col == 11662). Every well: [[TCN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
