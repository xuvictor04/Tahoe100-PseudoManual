---
symbol: "REEP1"
type: "gene"
col: 894
ensembl_id: "ENSG00000068615"
name: "receptor accessory protein 1"
location: "2p11.2"
module: 115
arm: "+"
pooled_cpm: 2.58
n_lines_expressing: 40
n_dd_up: 36
n_dd_down: 0
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 9
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# REEP1

*receptor accessory protein 1* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (13 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.86× (z +17.1, q 0e+00, up in 27 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.0516×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SNU-1 0.0841×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (J82 0.0892×); [[Tazarotene (drug)]] 0.5 µM in 1 line (BT-474 0.0599×); [[Vilanterol (drug)]] 0.05 µM in 1 line (RKO 0.0594×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTLL7]] (+0.57, fdr 3e-05), [[SYT7]] (+0.57, fdr 2e-04), [[NFASC]] (+0.55, fdr 1e-05); moves opposite to [[RSPRY1]] (-0.45, fdr 1e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 9 go from it, the strongest it → [[HRK]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 894.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.86×** | +17.1 | 0e+00 | 27/31 (NCI-H460, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.56×** | +13.6 | 2e-39 | 7/7 (A-427, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.82×** | +13.1 | 9e-37 | 14/22 (A549, BT-474, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.83×** | +12.0 | 6e-31 | 27/35 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.99×** | +11.9 | 2e-30 | 1/1 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.66×** | +11.6 | 5e-29 | 22/30 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.14×** | +10.2 | 1e-22 | 23/32 (NCI-H460, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.06×** | +10.0 | 1e-21 | 20/24 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.36×** | +10.0 | 1e-21 | 1/3 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.73×** | +9.0 | 2e-17 | 22/33 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.65×** | +8.7 | 2e-16 | 17/28 (LoVo, A549, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.68×** | +8.3 | 5e-15 | 17/24 (A549, LoVo, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.30×** | +7.4 | 5e-12 | 18/29 (LoVo, SW480, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.73×** | +6.1 | 3e-08 | 14/25 (LoVo, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +5.4 | 3e-06 | 2/13 (A-172, NCI-H460) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.74×** | +5.0 | 2e-05 | 12/20 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +4.3 | 6e-04 | 6/26 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.91×** | +4.1 | 0.001 | 1/28 (A549) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.60×** | +4.0 | 0.001 | 6/25 (LoVo, SW48, …) | rises with dose |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.0516×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SNU-1 0.0841×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (J82 0.0892×); [[Tazarotene (drug)]] 0.5 µM in 1 line (BT-474 0.0599×); [[Vilanterol (drug)]] 0.05 µM in 1 line (RKO 0.0594×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 894. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 21.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0516× (z -16.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 1.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.8× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 7.43 | 0 | 1 | — | [[Tazarotene (drug)]] 0.5 µM 0.0599× (z -9.0) |
| [[J82 (line)]] | alt | 5.05 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0892× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 1.28 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 15.4× (z +9.7) | — |
| [[RKO (line)]] | wt | 4.67 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0594× (z -8.5) |
| [[SNU-1 (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0841× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.696 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.673 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.681 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.708 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.570 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.583 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.750 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.664 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.550 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.649 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.647 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.520 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.679 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.586 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.704 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.563 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.950 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.676 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 894), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTLL7]] | +0.57 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[SYT7]] | +0.57 | +0.31 / +0.65 | both halves | 2e-04 |  |
| [[NFASC]] | +0.55 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[CACNB4]] | +0.55 | +0.36 / +0.55 | both halves | 9e-05 |  |
| [[LINC00937]] | +0.54 | +0.36 / +0.66 | both halves | 1e-04 |  |
| [[APBA1]] | +0.54 | +0.37 / +0.64 | both halves | 8e-05 |  |
| [[RHBDL3]] | +0.53 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[RETREG1]] | +0.53 | +0.55 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY; STRING 420 |
| [[CDH23]] | +0.53 | +0.45 / +0.70 | both halves | 3e-05 | pathway: Sensory Perception |
| [[TMEM266]] | +0.53 | +0.37 / +0.67 | both halves | 8e-05 |  |
| [[ROR2]] | +0.52 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[NXPE3]] | +0.52 | +0.44 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSPRY1]] | -0.45 | -0.34 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers REEP1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.7% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[KIF1A]] | B | KIF1A activity raises REEP1's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 1.67× lower at baseline in the lines without KIF1A | 0.050 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |
| [[DPYSL5]] | B | DPYSL5 activity raises REEP1's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 1.71× lower at baseline in the lines without DPYSL5 | 0.091 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[DOCK3]] | B | DOCK3 activity raises REEP1's level | lines that do not express DOCK3 (22) vs lines expressing it (28) | 1.72× lower at baseline in the lines without DOCK3 | 0.098 | ⚠ within organs, on part of the lines; also absent: RBM20, LHX2, ADCY1 |
| [[SEPTIN3]] | C | SEPTIN3 activity raises REEP1's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 1.97× lower at baseline in the lines without SEPTIN3 | 0.025 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HRK]] | B | REEP1 activity raises HRK's level | lines that do not express REEP1 (10) vs lines expressing it (40) | 1.82× lower at baseline in the lines without REEP1 | 0.044 | ⚠ within organs, on part of the lines; also absent: SEPTIN3; maybe low, not absent |
| [[ARHGAP44]] | B | REEP1 activity raises ARHGAP44's level | lines that do not express REEP1 (10) vs lines expressing it (40) | 2.38× lower at baseline in the lines without REEP1 | 0.047 | ⚠ within organs, on part of the lines; also absent: SEPTIN3; maybe low, not absent |
| [[TSPAN33]] | B | REEP1 activity raises TSPAN33's level | lines that do not express REEP1 (10) vs lines expressing it (40) | 1.57× lower at baseline in the lines without REEP1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SEPTIN3; maybe low, not absent |
| [[SLC26A5]] | B | REEP1 activity raises SLC26A5's level | lines that do not express REEP1 (10) vs lines expressing it (40) | 1.18× lower at baseline in the lines without REEP1 | 0.073 | ⚠ within organs, on part of the lines; also absent: SEPTIN3; maybe low, not absent |
| [[ABCC5]] | B | REEP1 activity raises ABCC5's level | lines that do not express REEP1 (10) vs lines expressing it (40) | 1.61× lower at baseline in the lines without REEP1 | 0.089 | ⚠ within organs, on part of the lines; also absent: SEPTIN3; maybe low, not absent |
| [[LINC00937]] | B | REEP1 activity raises LINC00937's level | lines that do not express REEP1 (10) vs lines expressing it (40) | 1.89× lower at baseline in the lines without REEP1 | 0.092 | ⚠ within organs, on part of the lines; also absent: SEPTIN3; maybe low, not absent |
| [[SPTB]] | B | REEP1 activity raises SPTB's level | lines that do not express REEP1 (10) vs lines expressing it (40) | 2.08× lower at baseline in the lines without REEP1 | 0.094 | ⚠ within organs, on part of the lines; also absent: SEPTIN3; maybe low, not absent |
| cells under [[Panobinostat (drug)]] 5 µM | B | REEP1 activity raises the cells' numbers under Panobinostat 5 µM (protects the cells) | lines that do not express REEP1 (10) vs lines expressing it (38) | the lines without REEP1: 0.78× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: SEPTIN3; maybe low, not absent |
| [[SEPTIN3]] | C | REEP1 activity raises SEPTIN3's level | lines that do not express REEP1 (10) vs lines expressing it (40) | 2.55× lower at baseline in the lines without REEP1 | 0.059 | ⚠ within organs, on part of the lines; also absent: SEPTIN3; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (4.2, 36.2); signed map (29.2, 28.8). **Vector** length 46.0, 7.28% of its response variance represented; |z| ≥ 3 in 862 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +17.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +10.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.9 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +8.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.9 | +8.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | +4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +6.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +1.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.3 | -0.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | +1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -2.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -2.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -0.2 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.6 | -0.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -0.6 | -1.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.6 | -2.1 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -0.6 | -1.5 |
|  | [[Megestrol (drug)]] 5 µM |  | -0.5 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | receptor accessory protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:86,213,993-86,338,083 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13110, SPG31, Yip2a; previously C2orf23 |
| Gene groups (HGNC) | Receptor accessory proteins |
| Hallmark sets | MYOGENESIS, ESTROGEN_RESPONSE_EARLY |
| Reactome | 3 pathways, smallest: Expression and translocation of olfactory receptors; Olfactory Signaling Pathway; Sensory Perception |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H902](https://www.uniprot.org/uniprotkb/Q9H902) (Receptor expression-enhancing protein 1):

> Required for endoplasmic reticulum (ER) network formation, shaping and remodeling; it links ER tubules to the cytoskeleton. May also enhance the cell surface expression of odorant receptors. May play a role in long-term axonal maintenance.

**Summary**, from NCBI Gene [65055](https://www.ncbi.nlm.nih.gov/gene/65055):

> This gene encodes a mitochondrial protein that functions to enhance the cell surface expression of odorant receptors. Mutations in this gene cause spastic paraplegia autosomal dominant type 31, a neurodegenerative disorder. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:25786](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25786) · Entrez [65055](https://www.ncbi.nlm.nih.gov/gene/65055) · UniProt [Q9H902](https://www.uniprot.org/uniprotkb/Q9H902) · Ensembl [ENSG00000068615](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068615)

## Data

Gene col 894: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 894); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 894, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 894]; `tensor/DDL_lfc|DDL_z.npy` [894]; `embed/gene_vectors.npy` [894]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 894 or target_col == 894). Every well: [[REEP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/REEP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
