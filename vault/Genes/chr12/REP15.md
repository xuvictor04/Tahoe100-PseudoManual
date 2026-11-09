---
symbol: "REP15"
type: "gene"
col: 10477
ensembl_id: "ENSG00000174236"
name: "RAB15 effector protein"
location: "12p11.22"
module: 47
arm: "+"
pooled_cpm: 2.5
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 12
n_dd_up_clean: 1
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 12
direction_downstream: 1
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# REP15

*RAB15 effector protein* — 12p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.83× (z +8.0, q 6e-13, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.37× (z +3.5, q 0.088, up in 3 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.527× (z -7.3, q 1e-10, down in 19 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BLZF2P]] (+0.65, fdr 7e-06), [[PARVG]] (+0.60, fdr 8e-06), [[A3GALT2]] (+0.56, fdr 1e-05); moves opposite to [[SP1]] (-0.54, fdr 4e-05), [[PPP1CB]] (-0.50, fdr 5e-05), [[ATXN2L]] (-0.45, fdr 4e-04).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[HTR7]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PPFIBP1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10477.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.83×** | +8.0 | 6e-13 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +3.8 | 0.041 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.088 | 3/42 (LOX-IMVI, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +3.4 | 0.088 | 3/12 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 1.31× | +3.0 | 0.26 | 3/37 (NCI-H1573, PANC-1, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10477.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.527×** | -7.3 | 1e-10 | 19/31 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.531×** | -5.1 | 8e-05 | 19/40 (LOX-IMVI, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.548×** | -4.9 | 2e-04 | 19/43 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.574×** | -4.5 | 9e-04 | 18/43 (A549, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.596×** | -4.2 | 0.002 | 17/39 (NCI-H1573, SW480, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.571×** | -4.2 | 0.002 | 12/41 (SK-MEL-2, SW48, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.593×** | -4.1 | 0.003 | 13/38 (A549, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.381×** | -4.1 | 0.003 | 14/34 (HOP62, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.615×** | -4.0 | 0.005 | 12/42 (CFPAC-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.677×** | -3.2 | 0.082 | 9/29 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.679×** | -3.2 | 0.082 | 8/40 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.681×** | -3.1 | 0.082 | 11/35 (C32, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10477. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 3.87 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0800× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 1.95 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0397× (z -8.5) |
| [[SW480 (line)]] | alt | 6.27 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -10.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.826 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.984 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.905 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.909 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.780 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.685 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.786 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.756 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10477), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLZF2P]] | +0.65 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[PARVG]] | +0.60 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[A3GALT2]] | +0.56 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[PPFIBP1]] | +0.53 | +0.49 / +0.56 | both halves | 1e-05 | ⚠ **readthrough risk**: this gene lies 0.9 kb 3′ of PPFIBP1 on the same strand (can correlate by spillover, not regulation) |
| [[BACH1]] | +0.52 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[BMP8A]] | +0.51 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[CDKL4]] | +0.51 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[C13orf46]] | +0.51 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[SLC25A51]] | +0.51 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[MSANTD1]] | +0.49 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[MOCS2-DT]] | +0.49 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[NTRK1]] | +0.49 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[LRP2BP-AS1]] | +0.48 | +0.50 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SP1]] | -0.54 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[PPP1CB]] | -0.50 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[ATXN2L]] | -0.45 | -0.24 / -0.45 | both halves | 4e-04 |  |
| [[THAP8]] | -0.44 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[LSM14B]] | -0.44 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[ALDH3B1]] | -0.42 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[DVL2]] | -0.42 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[FTH1]] | -0.41 | -0.39 / -0.30 | both halves | 2e-04 |  |
| [[ZBTB7B]] | -0.41 | -0.24 / -0.45 | both halves | 5e-04 |  |
| [[EGLN1]] | -0.41 | -0.30 / -0.36 | both halves | 2e-04 |  |
| [[THBS3]] | -0.41 | -0.40 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HTR7]] | B | HTR7 activity raises REP15's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 1.34× lower at baseline in the lines without HTR7 | 0.008 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[CDH13]] | B | CDH13 activity raises REP15's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 1.62× lower at baseline in the lines without CDH13 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[FRMD4A]] | B | FRMD4A activity raises REP15's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 1.51× lower at baseline in the lines without FRMD4A | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[HS3ST3A1]] | B | HS3ST3A1 activity raises REP15's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 1.57× lower at baseline in the lines without HS3ST3A1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1 |
| [[ITGA2]] | B | ITGA2 activity raises REP15's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 1.34× lower at baseline in the lines without ITGA2 | 0.041 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[C13orf46]] | B | C13orf46 activity raises REP15's level | lines that do not express C13orf46 (11) vs lines expressing it (39) | 1.52× lower at baseline in the lines without C13orf46 | 0.050 | ⚠ within organs, on part of the lines; also absent: RASA3, COL27A1, PRR5L |
| [[C12orf75-AS1]] | B | C12orf75-AS1 activity raises REP15's level | lines that do not express C12orf75-AS1 (22) vs lines expressing it (28) | 1.33× lower at baseline in the lines without C12orf75-AS1 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1 |
| [[PARVG]] | B | PARVG activity raises REP15's level | lines that do not express PARVG (15) vs lines expressing it (35) | 1.39× lower at baseline in the lines without PARVG | 0.066 | ⚠ within organs, on part of the lines; also absent: PARVB, DCLK2, RASSF8 |
| [[FLT1]] | B | FLT1 activity raises REP15's level | lines that do not express FLT1 (28) vs lines expressing it (22) | 1.50× lower at baseline in the lines without FLT1 | 0.085 | ⚠ within organs, on part of the lines; also absent: ZNF365, COL19A1, PDGFRB |
| [[LINC02813]] | B | LINC02813 activity raises REP15's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 1.27× lower at baseline in the lines without LINC02813 | 0.091 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN |
| [[NTM]] | B | NTM activity raises REP15's level | lines that do not express NTM (33) vs lines expressing it (17) | 1.47× lower at baseline in the lines without NTM | 0.097 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1 |
| [[PPFIBP1]] | C | PPFIBP1's natural level strengthens REP15's drug response | PPFIBP1's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.65; direction not clear | 0.064 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPFIBP1]] | C | REP15's natural level strengthens PPFIBP1's drug response | REP15's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.67; direction not clear | 0.047 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.399). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.1, -15.2); signed map (15.8, 16.3). **Vector** length 45.5, 5.62% of its response variance represented; |z| ≥ 3 in 988 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.3 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +1.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +2.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.4 | -0.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.3 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +2.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.0 | +2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.0 | +2.6 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -1.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | RAB15 effector protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.22 — chr12:27,696,447-27,697,596 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RAB15EP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6BDI9](https://www.uniprot.org/uniprotkb/Q6BDI9) (Rab15 effector protein):

> Effector that interacts with Rab GTPases in their active form (GTP-bound) including RAB15, RAB3A-D and RAB34. Controls downstream signaling such as cell proliferation and cell migration. Also regulates transferrin receptor recycling from the endocytic recycling compartment.

**Summary**, from NCBI Gene [387849](https://www.ncbi.nlm.nih.gov/gene/387849):

> The protein encoded by this intronless gene interacts with GTP-bound Rab15 and is involved in recycling of transferrin receptor from the endocytic recycling compartment to the cell surface. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:33748](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33748) · Entrez [387849](https://www.ncbi.nlm.nih.gov/gene/387849) · UniProt [Q6BDI9](https://www.uniprot.org/uniprotkb/Q6BDI9) · Ensembl [ENSG00000174236](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174236)

## Data

Gene col 10477: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10477); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10477, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10477]; `tensor/DDL_lfc|DDL_z.npy` [10477]; `embed/gene_vectors.npy` [10477]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10477 or target_col == 10477). Every well: [[REP15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/REP15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
