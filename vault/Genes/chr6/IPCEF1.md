---
symbol: "IPCEF1"
type: "gene"
col: 1090
ensembl_id: "ENSG00000074706"
name: "interaction protein for cytohesin exchange factors 1"
location: "6q25.2"
module: 150
arm: "+"
pooled_cpm: 4.09
n_lines_expressing: 45
n_dd_up: 26
n_dd_down: 8
n_dd_up_clean: 19
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/150"]
generated_by: "tahoemap"
---

# IPCEF1

*interaction protein for cytohesin exchange factors 1* — 6q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.47× (z +28.9, q 0e+00, up in 27 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.525× (z -7.1, q 1e-09, down in 16 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.667× (z -4.4, q 0.002, down in 14 of 38 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02268]] (+0.73, fdr 1e-05), [[NEB]] (+0.69, fdr 2e-05), [[ARHGAP15]] (+0.68, fdr 1e-05).
> It is in [[Module 150]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1090.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.47×** | +28.9 | 0e+00 | 27/31 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.56×** | +23.5 | 0e+00 | 27/30 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.92×** | +15.0 | 0e+00 | 24/29 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +10.3 | 1e-22 | 3/9 (NCI-H2030, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.38×** | +9.5 | 2e-19 | 6/17 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.69×** | +8.1 | 4e-14 | 15/40 (PANC-1, A498, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +7.9 | 3e-13 | 19/40 (A-172, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +6.2 | 3e-08 | 2/10 (PANC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +5.8 | 5e-07 | 12/31 (HEC-1-A, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.7 | 7e-07 | 8/41 (HEC-1-A, BT-474, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +5.0 | 3e-05 | 10/29 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +4.8 | 8e-05 | 11/37 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +4.6 | 2e-04 | 10/36 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.45×** | +4.1 | 0.002 | 5/36 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.46×** | +3.9 | 0.003 | 9/36 (A-172, A549, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +3.8 | 0.005 | 14/35 (NCI-H1792, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +3.7 | 0.006 | 6/37 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.43×** | +3.6 | 0.008 | 2/24 (SK-MEL-2, A549) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.010 | 10/36 (A549, A498, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.019 | 5/39 (J82, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1090.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.525×** | -7.1 | 1e-09 | 16/24 (SK-MEL-2, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.587×** | -5.8 | 1e-06 | 18/41 (SHP-77, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.667×** | -4.4 | 0.002 | 14/38 (HS-578T, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.703×** | -3.9 | 0.016 | 15/40 (RPMI-7951, SW 900, …) | all doses, stronger at high dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | **0.723×** | -3.6 | 0.043 | 7/35 (H4, HepG2/C3A, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.736×** | -3.4 | 0.075 | 9/40 (AN3 CA, SHP-77, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 0.05 µM |  | **0.725×** | -3.3 | 0.090 | 6/33 (Panc 03.27, J82, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.745×** | -3.2 | 0.090 | 8/40 (HEC-1-A, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1090. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 25.4 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0610× (z -12.9) ⚠ toxic; cell-cycle shift, explains ~64% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0939× (z -10.9) |
| [[C32 (line)]] | wt | 2.75 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 57.9× (z +13.8) | — |
| [[HS-578T (line)]] | alt | 5.21 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +12.9) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0514× (z -10.0) |
| [[LoVo (line)]] | wt | 1.48 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.5× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 7.26 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.22× (z +12.6) | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0766× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 1.26 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +10.3) | — |
| [[SNU-423 (line)]] | alt | 3.86 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +11.1) | — |
| [[A-172 (line)]] | wt | 11.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +8.6) | — |
| [[A498 (line)]] | wt | 4.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.42× (z +10.5) | — |
| [[BT-474 (line)]] | alt | 2.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.3× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 2.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.75× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 5.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.25× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 1.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.1× (z +11.8) | — |
| [[Hs 766T (line)]] | wt | 1.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.0× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 5.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 33.8× (z +12.8) | — |
| [[J82 (line)]] | alt | 2.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.4× (z +10.8) | — |
| [[RPMI-7951 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0564× (z -9.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SHP-77 (line)]] | alt | 45.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.149× (z -9.0) |
| [[SW480 (line)]] | alt | 1.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.58× (z +8.5) | — |
| [[A-427 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.966 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.991 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.959 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.907 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1090), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02268]] | +0.73 | +0.75 / +0.50 | both halves | 1e-05 |  |
| [[NEB]] | +0.69 | +0.75 / +0.47 | both halves | 2e-05 |  |
| [[ARHGAP15]] | +0.68 | +0.72 / +0.49 | both halves | 1e-05 | same gene group |
| [[ANGPT2]] | +0.67 | +0.74 / +0.37 | both halves | 8e-05 |  |
| [[COL21A1]] | +0.66 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[MYO16]] | +0.66 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[TG]] | +0.66 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[LINC00486]] | +0.65 | +0.73 / +0.42 | both halves | 4e-05 |  |
| [[PECAM1]] | +0.65 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[THSD7B]] | +0.64 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[HEATR4]] | +0.64 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[DRAIC]] | +0.64 | +0.68 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers IPCEF1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TEX41]] | B | TEX41 activity raises IPCEF1's level | lines that do not express TEX41 (29) vs lines expressing it (21) | 1.90× lower at baseline in the lines without TEX41 | 0.077 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12 |
| [[RNF32-DT]] | B | RNF32-DT activity lowers IPCEF1's level | lines that do not express RNF32-DT (5) vs lines expressing it (45) | 2.12× higher at baseline in the lines without RNF32-DT | 0.088 | ⚠ within organs, on part of the lines; also absent: SPATA13; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 150]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.749). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.5, 22.2); signed map (26.7, 12.7). **Vector** length 65.3, 10.5% of its response variance represented; |z| ≥ 3 in 1,066 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.0 | +28.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +23.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +10.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +15.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +5.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +2.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.8 | +3.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -0.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.3 | -3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.8 | +0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | +0.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -0.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | interaction protein for cytohesin exchange factors 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.2 — chr6:154,154,496-154,356,803 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PIP3-E, KIAA0403 |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWN9](https://www.uniprot.org/uniprotkb/Q8WWN9) (Interactor protein for cytohesin exchange factors 1):

> Enhances the promotion of guanine-nucleotide exchange by PSCD2 on ARF6 in a concentration-dependent manner.

**Summary**, from NCBI Gene [26034](https://www.ncbi.nlm.nih.gov/gene/26034):

> Predicted to enable peroxidase activity and protein-macromolecule adaptor activity. Predicted to be involved in enzyme-linked receptor protein signaling pathway and response to oxidative stress. Predicted to be located in cytoplasm and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21204](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21204) · Entrez [26034](https://www.ncbi.nlm.nih.gov/gene/26034) · UniProt [Q8WWN9](https://www.uniprot.org/uniprotkb/Q8WWN9) · Ensembl [ENSG00000074706](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074706)

## Data

Gene col 1090: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1090); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1090, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1090]; `tensor/DDL_lfc|DDL_z.npy` [1090]; `embed/gene_vectors.npy` [1090]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1090 or target_col == 1090). Every well: [[IPCEF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IPCEF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
