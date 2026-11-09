---
symbol: "RNLS"
type: "gene"
col: 11570
ensembl_id: "ENSG00000184719"
name: "renalase, FAD dependent amine oxidase"
location: "10q23.31"
module: 10
arm: "+"
pooled_cpm: 9.39
n_lines_expressing: 30
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# RNLS

*renalase, FAD dependent amine oxidase* — 10q23.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.08× (z +12.9, q 3e-35, up in 13 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.597× (z -6.4, q 6e-08, down in 19 of 28 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SK-MEL-2 0.205×, NCI-H1792 0.205×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.111×, PANC-1 0.205×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.133×; ⚠ cell-cycle shift, explains ~0% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (LS 180 0.0559×).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLIC2]] (+0.69, fdr 1e-05), [[LINC01725]] (+0.68, fdr 1e-05), [[CPEB1]] (+0.66, fdr 1e-05); moves opposite to [[DHTKD1]] (-0.62, fdr 5e-05), [[GNAI2]] (-0.56, fdr 2e-04), [[ATG16L2]] (-0.52, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); 2 go from it, the strongest it → [[LINC01239]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11570.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +12.9 | 3e-35 | 13/27 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +8.8 | 5e-16 | 6/16 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.82×** | +7.5 | 1e-11 | 13/27 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +7.5 | 1e-11 | 5/20 (A549, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.47×** | +6.8 | 1e-09 | 18/28 (NCI-H1792, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +6.5 | 8e-09 | 7/24 (SW 900, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +6.2 | 4e-08 | 14/27 (NCI-H2347, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +5.2 | 2e-05 | 9/27 (NCI-H2347, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.7 | 2e-04 | 8/28 (SW480, HT-29, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +4.2 | 0.002 | 7/28 (Panc 03.27, NCI-H460, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.41×** | +4.1 | 0.002 | 8/28 (SK-MEL-2, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +3.9 | 0.004 | 10/27 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.38×** | +3.8 | 0.007 | 8/27 (SK-MEL-2, HS-578T, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.015 | 14/28 (NCI-H1573, NCI-H2347, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.31×** | +3.4 | 0.026 | 9/27 (SK-MEL-2, HS-578T, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.093 | 9/28 (NCI-H2347, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11570.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SK-MEL-2 0.205×, NCI-H1792 0.205×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.111×, PANC-1 0.205×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.133×; ⚠ cell-cycle shift, explains ~0% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (LS 180 0.0559×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.597×** | -6.4 | 6e-08 | 19/28 (A498, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.692×** | -4.6 | 0.001 | 15/28 (A498, SW480, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.757×** | -3.5 | 0.097 | 12/28 (PANC-1, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.779× | -3.1 | 0.25 | 19/28 (A498, MIA PaCa-2, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11570. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 72.7 | 0 | 3 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 12.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +13.8) | — |
| [[PANC-1 (line)]] | alt | 13.4 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.203× (z -9.0) ⚠ cell-cycle shift, explains ~62% of this change |
| [[A-172 (line)]] | wt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +9.9) | — |
| [[A498 (line)]] | wt | 28.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.270× (z -9.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LS 180 (line)]] | wt | 8.43 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0559× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.111× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[NCI-H1792 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 2.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.52× (z +9.4) | — |
| [[SW1417 (line)]] | alt | 8.00 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0820× (z -11.0) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 13.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11570), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLIC2]] | +0.69 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[LINC01725]] | +0.68 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[CPEB1]] | +0.66 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[ANKRD18B]] | +0.63 | +0.45 / +0.24 | both halves | 5e-04 |  |
| [[KCNMB3]] | +0.63 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[GRIP1]] | +0.61 | +0.38 / +0.40 | both halves | 7e-05 |  |
| [[SATB1-AS1]] | +0.61 | +0.52 / +0.30 | both halves | 2e-04 |  |
| [[CCDC169]] | +0.61 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[CC2D2A]] | +0.60 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[PATL2]] | +0.59 | +0.52 / +0.34 | both halves | 1e-04 |  |
| [[GPR158]] | +0.58 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[LINC00240]] | +0.57 | +0.50 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHTKD1]] | -0.62 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[GNAI2]] | -0.56 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[ATG16L2]] | -0.52 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[EVI5L]] | -0.52 | -0.21 / -0.34 | both halves | 7e-04 |  |
| [[CHPF]] | -0.52 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[CABLES2]] | -0.52 | -0.29 / -0.24 | both halves | 5e-04 |  |
| [[TRAPPC1]] | -0.52 | -0.44 / -0.21 | both halves | 7e-04 |  |
| [[NPHP4]] | -0.52 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[SRGAP2D]] | -0.52 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[WDFY2]] | -0.51 | -0.42 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises RNLS's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01239]] | B | RNLS activity raises LINC01239's level | lines that do not express RNLS (20) vs lines expressing it (30) | 2.64× lower at baseline in the lines without RNLS | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP5, MAF, NAV1; maybe low, not absent |
| [[ATP6V1E2]] | B | RNLS activity lowers ATP6V1E2's level | lines that do not express RNLS (20) vs lines expressing it (30) | 1.46× higher at baseline in the lines without RNLS | 0.099 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP5, MAF, NAV1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.566). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (27.1, 24.8); signed map (39.1, 19.7). **Vector** length 55.8, 11.0% of its response variance represented; |z| ≥ 3 in 627 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +12.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.9 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +1.3 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.0 | -6.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -0.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.1 | -4.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -1.8 | -3.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | renalase, FAD dependent amine oxidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.31 — chr10:88,273,864-88,584,530 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11218, renalase; previously C10orf59 |
| Gene groups (HGNC) | Flavoproteins; Oxidoreductases |
| Reactome | 3 pathways, smallest: Nicotinate metabolism; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VYX0](https://www.uniprot.org/uniprotkb/Q5VYX0) (Renalase):

> Catalyzes the oxidation of the less abundant 1,2-dihydro-beta-NAD(P) and 1,6-dihydro-beta-NAD(P) to form beta-NAD(P)(+). The enzyme hormone is secreted by the kidney, and circulates in blood and modulates cardiac function and systemic blood pressure. Lowers blood pressure in vivo by decreasing cardiac contractility and heart rate and preventing a compensatory increase in peripheral vascular tone, suggesting a causal link to the increased plasma catecholamine and heightened cardiovascular risk. …

**Summary**, from NCBI Gene [55328](https://www.ncbi.nlm.nih.gov/gene/55328):

> Enables several functions, including NADH binding activity; epinephrine binding activity; and monoamine oxidase activity. Involved in negative regulation of blood pressure and negative regulation of heart rate. Located in extracellular region. Implicated in essential hypertension; hypertension; and stroke. Biomarker of end stage renal disease. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25641](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25641) · Entrez [55328](https://www.ncbi.nlm.nih.gov/gene/55328) · UniProt [Q5VYX0](https://www.uniprot.org/uniprotkb/Q5VYX0) · Ensembl [ENSG00000184719](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184719)

## Data

Gene col 11570: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11570); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11570, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11570]; `tensor/DDL_lfc|DDL_z.npy` [11570]; `embed/gene_vectors.npy` [11570]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11570 or target_col == 11570). Every well: [[RNLS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNLS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
