---
symbol: "PHETA1"
type: "gene"
col: 12571
ensembl_id: "ENSG00000198324"
name: "PH domain containing endocytic trafficking adaptor 1"
location: "12q24.12"
module: 2
arm: "+"
pooled_cpm: 2.25
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 2
n_dd_up_clean: 20
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# PHETA1

*PH domain containing endocytic trafficking adaptor 1* — 12q24.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.33× (z +21.5, q 0e+00, up in 30 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Artesunate (drug)]] 0.5 µM: 0.654× (z -3.9, q 0.034, down in 9 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Procainamide (hydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H460 0.0549×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (PANC-1 0.0801×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 0.0904×; ⚠ toxic; cell-cycle shift, explains ~59% of this change); [[Valdecoxib (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0922×).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM38]] (+0.57, fdr 1e-05), [[LRWD1]] (+0.55, fdr 1e-05), [[NSMF]] (+0.55, fdr 2e-05); moves opposite to [[ICE2]] (-0.50, fdr 0.001, ⚠ one half only (not replicated)), [[PPA2]] (-0.47, fdr 1e-04), [[MRPS10]] (-0.45, fdr 5e-04), [[UFSP2]] (-0.43, fdr 5e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12571.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.33×** | +21.5 | 0e+00 | 30/31 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.93×** | +12.4 | 8e-33 | 38/44 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.81×** | +12.1 | 2e-31 | 35/43 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.00×** | +9.9 | 4e-21 | 35/44 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.76×** | +8.8 | 1e-16 | 12/24 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.67×** | +8.5 | 1e-15 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +6.5 | 5e-09 | 13/29 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +5.5 | 2e-06 | 1/3 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.84×** | +5.5 | 2e-06 | 3/11 (LS 180, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +4.9 | 5e-05 | 2/42 (AsPC-1, CFPAC-1) | top dose only | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +4.4 | 5e-04 | 9/30 (HepG2/C3A, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +4.3 | 9e-04 | 11/45 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +4.1 | 0.002 | 9/44 (A498, SK-MEL-2, …) | rises with dose | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.30×** | +3.9 | 0.003 | 0/3 | rises with dose | noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +3.7 | 0.009 | 2/11 (AsPC-1, HEC-1-A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.50×** | +3.6 | 0.010 | 4/27 (A498, PANC-1, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.013 | 6/44 (PANC-1, CFPAC-1, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.47×** | +3.5 | 0.017 | 3/43 (Panc 03.27, A-172, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.46×** | +3.2 | 0.037 | 4/40 (hTERT-HPNE, A498, …) | inconsistent across doses |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.037 | 4/23 (NCI-H2347, A-427, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12571.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Procainamide (hydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H460 0.0549×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (PANC-1 0.0801×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 0.0904×; ⚠ toxic; cell-cycle shift, explains ~59% of this change); [[Valdecoxib (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0922×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | **0.654×** | -3.9 | 0.034 | 9/44 (SW48, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Penfluridol (drug)]] 5 µM |  | **0.647×** | -3.8 | 0.034 | 11/33 (HepG2/C3A, J82, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.505× | -3.3 | 0.20 | 10/35 (NCI-H2030, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12571. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1.95 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.56× (z +9.7) | [[Procainamide (hydrochloride) (drug)]] 0.5 µM 0.0549× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 5.68 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0904× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~59% of this change |
| [[HepG2_C3A (line)]] | wt | 10.5 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0922× (z -8.7) |
| [[LoVo (line)]] | wt | 3.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.95× (z +11.8) | — |
| [[LS 180 (line)]] | wt | 4.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.96× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 1.61 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0801× (z -8.9) |
| [[SW480 (line)]] | alt | 2.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.90× (z +10.5) | — |
| [[A-172 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12571), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM38]] | +0.57 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[LRWD1]] | +0.55 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[NSMF]] | +0.55 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[ADCK5]] | +0.53 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[LFNG]] | +0.52 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[SLC9A3-AS1]] | +0.51 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[PSD]] | +0.51 | +0.28 / +0.72 | both halves | 3e-04 | same gene group |
| [[LRRC56]] | +0.51 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[KLHL17]] | +0.50 | +0.34 / +0.49 | both halves | 1e-04 |  |
| [[DGKQ]] | +0.50 | +0.36 / +0.53 | both halves | 1e-04 |  |
| [[PLA2G4B]] | +0.50 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[PNP]] | +0.50 | +0.47 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ICE2]] | -0.50 | -0.16 / -0.52 | ⚠ one half (not replicated) | 0.001 |  |
| [[PPA2]] | -0.47 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[MRPS10]] | -0.45 | -0.23 / -0.54 | both halves | 5e-04 |  |
| [[UFSP2]] | -0.43 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[DPP8]] | -0.42 | -0.10 / -0.53 | ⚠ one half (not replicated) | 0.003 |  |
| [[NDUFS1]] | -0.42 | -0.19 / -0.48 | ⚠ not reproduced | 8e-04 |  |
| [[SRP72]] | -0.42 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[MRPL19]] | -0.42 | -0.33 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PHETA1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.454). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-9.7, -24.7); signed map (-5.0, 30.3). **Vector** length 41.5, 4.35% of its response variance represented; |z| ≥ 3 in 1,111 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +21.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +5.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.0 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +5.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +2.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +2.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +2.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.5 | +2.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -3.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.4 | -1.3 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.2 | -1.3 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.2 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | PH domain containing endocytic trafficking adaptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.12 — chr12:111,360,651-111,369,121 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32356, SES1, IPIP27A; previously FAM109A |
| Gene groups (HGNC) | Pleckstrin homology domain containing; PH domain containing endocytic trafficking adaptor family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N4B1](https://www.uniprot.org/uniprotkb/Q8N4B1) (Sesquipedalian-1):

> Plays a role in endocytic trafficking. Required for receptor recycling from endosomes, both to the trans-Golgi network and the plasma membrane.

**Summary**, from NCBI Gene [144717](https://www.ncbi.nlm.nih.gov/gene/144717):

> This gene encodes a protein that localizes to the endosome and interacts with the enzyme, inositol polyphosphate 5-phosphatase OCRL-1. Alternate splicing results in multiple transcript variants. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:26509](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26509) · Entrez [144717](https://www.ncbi.nlm.nih.gov/gene/144717) · UniProt [Q8N4B1](https://www.uniprot.org/uniprotkb/Q8N4B1) · Ensembl [ENSG00000198324](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198324)

## Data

Gene col 12571: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12571); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12571, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12571]; `tensor/DDL_lfc|DDL_z.npy` [12571]; `embed/gene_vectors.npy` [12571]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12571 or target_col == 12571). Every well: [[PHETA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHETA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
