---
symbol: "C4orf46"
type: "gene"
col: 12956
ensembl_id: "ENSG00000205208"
name: "chromosome 4 open reading frame 46"
location: "4q32.1"
module: 6
arm: "+"
pooled_cpm: 4.78
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# C4orf46

*chromosome 4 open reading frame 46* — 4q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (27 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.43× (z +13.8, q 1e-40, up in 34 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[5-Azacytidine (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0477×); [[Nimesulide (drug)]] 5 µM in 1 line (RKO 0.0978×; ⚠ toxic; unreliable plate only); [[Bortezomib (drug)]] 0.05 µM in 1 line (KATO III 0.0650×; ⚠ cell-cycle shift, explains ~53% of this change); [[Decitabine (drug)]] 0.05 µM in 1 line (RKO 0.0916×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOXM1]] (+0.74, fdr 7e-06), [[PKMYT1]] (+0.74, fdr 7e-06), [[EZH2]] (+0.71, fdr 7e-06); moves opposite to [[DDX27]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TCF19]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 27 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 27 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12956.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.43×** | +13.8 | 1e-40 | 34/40 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **2.09×** | +7.8 | 2e-12 | 20/29 (A-172, A-427, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | **1.89×** | +6.8 | 3e-09 | 4/8 (HOP62, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.81×** | +6.5 | 1e-08 | 24/47 (NCI-H1792, RKO, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.79×** | +6.4 | 2e-08 | 20/39 (PANC-1, J82, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.73×** | +6.0 | 1e-07 | 9/27 (A-172, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.71×** | +5.9 | 3e-07 | 16/47 (PANC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.65×** | +5.5 | 3e-06 | 14/40 (LoVo, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.63×** | +5.4 | 4e-06 | 7/26 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.66×** | +5.4 | 5e-06 | 13/38 (HEC-1-A, SW480, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.59×** | +5.1 | 2e-05 | 12/47 (NCI-H460, Panc 03.27, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **1.50×** | +4.3 | 9e-04 | 8/26 (KATO III, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.46×** | +4.2 | 0.001 | 12/47 (NCI-H1573, NCI-H460, …) | all doses, flat | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.48×** | +4.1 | 0.001 | 14/41 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.44×** | +4.0 | 0.002 | 8/46 (PANC-1, J82, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.055 | 12/48 (HOP62, A-172, …) | inconsistent across doses | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.66×** | +2.9 | 0.073 | 3/29 (NCI-H460, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12956.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[5-Azacytidine (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0477×); [[Nimesulide (drug)]] 5 µM in 1 line (RKO 0.0978×; ⚠ toxic; unreliable plate only); [[Bortezomib (drug)]] 0.05 µM in 1 line (KATO III 0.0650×; ⚠ cell-cycle shift, explains ~53% of this change); [[Decitabine (drug)]] 0.05 µM in 1 line (RKO 0.0916×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.715× | -3.5 | 0.27 | 16/44 (KATO III, NCI-H2347, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.916× | -3.2 | 0.37 | 6/48 (RPMI-7951, SK-MEL-2, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.822× | -3.1 | 0.37 | 10/47 (Panc 03.27, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Rifaximin (drug)]] 5 µM |  | 0.753× | -3.0 | 0.37 | 5/45 (A-172, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.70 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12956. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 7.33 | 0 | 2 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0978× (z -9.0) ⚠ toxic; unreliable plate only · without an alert: [[Decitabine (drug)]] 0.05 µM 0.0916× (z -8.6) |
| [[A549 (line)]] | wt | 3.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.16× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 5.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.14× (z +10.4) | — |
| [[KATO III (line)]] | alt | 4.09 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0650× (z -8.9) ⚠ cell-cycle shift, explains ~53% of this change |
| [[LoVo (line)]] | wt | 2.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.17× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 5.24 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0477× (z -9.1) |
| [[A-172 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.45 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12956), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXM1]] | +0.74 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[PKMYT1]] | +0.74 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[EZH2]] | +0.71 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[CENPM]] | +0.70 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[RAD54L]] | +0.69 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[TMPO]] | +0.69 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[RAD51AP1]] | +0.69 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[ZWINT]] | +0.69 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[E2F8]] | +0.68 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[KIF22]] | +0.67 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[SPC25]] | +0.67 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[FBXO5]] | +0.67 | +0.62 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX27]] | -0.61 | -0.56 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF19]] | B | TCF19 activity raises C4orf46's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 1.53× lower at baseline in the lines without TCF19 | 0.033 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers C4orf46's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CDC25A]] | B | CDC25A activity raises C4orf46's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.72× lower at baseline in the lines without CDC25A | 0.068 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[PBK]] | C | PBK activity raises C4orf46's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.12× lower at baseline in the lines without PBK | 0.021 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises C4orf46's level | lines that do not express AURKB (4) vs lines expressing it (46) | 1.98× lower at baseline in the lines without AURKB | 0.030 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[MELK]], [[TK1]] | C | MELK, TK1 activity raises C4orf46's level | lines that do not express MELK, TK1 (3) vs lines expressing them (47) | 2.27× lower at baseline in the lines without MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[DSCC1]] | C | DSCC1 activity raises C4orf46's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.85× lower at baseline in the lines without DSCC1 | 0.061 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[CDCA3]] | C | CDCA3 activity raises C4orf46's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 2.09× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.667). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.9, -45.2); signed map (-39.2, -46.7). **Vector** length 65.0, 10.1% of its response variance represented; |z| ≥ 3 in 879 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.51 to 65); *DNA strand elongation* (reactome, mean cos +0.51 to 28); *DNA Replication* (reactome, mean cos +0.50 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +13.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | +3.5 | +7.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | +2.7 | +6.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +2.5 | +5.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +2.3 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.5 | +2.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.3 | +2.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.3 | +1.4 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | -3.6 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +1.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -1.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.6 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 4 open reading frame 46 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.1 — chr4:158,666,675-158,672,255 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LOC201725, RCDG1 |
| Matched by | ensembl_id |

UniProt [Q504U0](https://www.uniprot.org/uniprotkb/Q504U0) carries no function annotation.

**Summary**, from NCBI Gene [201725](https://www.ncbi.nlm.nih.gov/gene/201725):

> This gene encodes a small, conserved protein of unknown function that is expressed in a variety of tissues. There are pseudogenes for this gene on chromosomes 6, 8, 16, and X. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2013]

**Accessions** — [HGNC:27320](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27320) · Entrez [201725](https://www.ncbi.nlm.nih.gov/gene/201725) · UniProt [Q504U0](https://www.uniprot.org/uniprotkb/Q504U0) · Ensembl [ENSG00000205208](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205208)

## Data

Gene col 12956: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12956); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12956, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12956]; `tensor/DDL_lfc|DDL_z.npy` [12956]; `embed/gene_vectors.npy` [12956]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12956 or target_col == 12956). Every well: [[C4orf46 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C4orf46.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
