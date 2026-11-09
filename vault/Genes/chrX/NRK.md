---
symbol: "NRK"
type: "gene"
col: 4444
ensembl_id: "ENSG00000123572"
name: "Nik related kinase"
location: "Xq22.3"
module: 66
arm: "+"
pooled_cpm: 2.57
n_lines_expressing: 10
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# NRK

*Nik related kinase* — Xq22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.94× (z +11.6, q 3e-28, up in 4 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.29× (z +9.8, q 3e-20, up in 3 of 5 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Erlotinib (drug)]] 0.05 µM: 0.509× (z -3.7, q 0.099, down in 0 of 6 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (BT-474 0.0805×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFEMP1]] (+0.58, fdr 4e-05), [[BHMT2]] (+0.58, fdr 4e-05), [[CHRDL1]] (+0.55, fdr 2e-05); moves opposite to [[SNAPC2]] (-0.48, fdr 1e-04), [[PMM1]] (-0.48, fdr 2e-04), [[ZNHIT3]] (-0.47, fdr 1e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NEMP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4444.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.94×** | +11.6 | 3e-28 | 4/5 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.38×** | +10.8 | 2e-24 | 5/5 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.29×** | +9.8 | 3e-20 | 3/5 (NCI-H2347, HOP62, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.59×** | +9.2 | 4e-18 | 3/5 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.70×** | +5.7 | 1e-06 | 1/5 (HOP62) | top dose only | cell-cycle shift (explains ~4% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.75×** | +5.5 | 4e-06 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.37×** | +5.0 | 5e-05 | 0/5 | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.44×** | +5.0 | 5e-05 | 2/4 (NCI-H2347, SNU-423) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +4.9 | 5e-05 | 2/5 (NCI-H2347, SNU-423) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.34×** | +4.9 | 5e-05 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **2.12×** | +4.3 | 7e-04 | 0/5 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.15×** | +4.2 | 0.001 | 1/5 (NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +4.2 | 0.001 | 6/7 (NCI-H2347, BT-474, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +4.0 | 0.003 | 5/5 (HOP62, J82, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.62×** | +3.9 | 0.003 | 0/7 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.50×** | +3.8 | 0.005 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.89×** | +3.7 | 0.007 | 1/5 (BT-474) | inconsistent across doses | position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | **1.79×** | +3.4 | 0.024 | 0/5 | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +3.3 | 0.030 | 3/5 (SNU-423, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.48×** | +3.2 | 0.043 | 1/7 (SNU-423) | top dose only | position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **1.71×** | +3.1 | 0.051 | 0/6 | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.69×** | +3.0 | 0.061 | 0/5 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.08×** | +3.0 | 0.061 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.64×** | +2.9 | 0.094 | 1/6 (HOP62) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4444.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (BT-474 0.0805×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Erlotinib (drug)]] 0.05 µM |  | **0.509×** | -3.7 | 0.099 | 0/6 | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.850× | -3.6 | 0.099 | 1/7 (HOP62) | inconsistent across doses |  |
| [[Vortioxetine (drug)]] 0.5 µM |  | 0.581× | -3.2 | 0.27 | 0/7 | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | 0.567× | -3.1 | 0.29 | 0/6 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4444. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 10.1 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0805× (z -8.9) |
| [[A-172 (line)]] | wt | 0.233 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.181 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.193 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.233 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.331 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.255 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.255 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.233 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.239 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.347 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.257 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.257 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.268 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.225 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.220 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.281 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.920 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.211 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.261 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.226 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.210 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.217 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.281 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.223 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.225 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.209 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.219 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.221 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.215 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.243 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.301 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.252 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.237 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.278 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.230 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4444), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFEMP1]] | +0.58 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[BHMT2]] | +0.58 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[CHRDL1]] | +0.55 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[CDH6]] | +0.54 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[PLCB4]] | +0.53 | +0.37 / +0.54 | both halves | 7e-05 |  |
| [[MOXD1]] | +0.53 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[EDIL3-DT]] | +0.50 | +0.39 / +0.51 | both halves | 6e-05 |  |
| [[ADAMTS3]] | +0.50 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[HAVCR1]] | +0.49 | +0.26 / +0.50 | both halves | 3e-04 |  |
| [[CNN3-DT]] | +0.49 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[CDH2]] | +0.49 | +0.39 / +0.54 | both halves | 6e-05 |  |
| [[XK]] | +0.49 | +0.36 / +0.44 | both halves | 9e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAPC2]] | -0.48 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[PMM1]] | -0.48 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[ZNHIT3]] | -0.47 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[SPATA2L]] | -0.46 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[NOSIP]] | -0.46 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[SCNM1]] | -0.46 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[RCE1]] | -0.45 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[LMBR1L]] | -0.45 | -0.45 / -0.37 | both halves | 9e-05 |  |
| [[ZNF611]] | -0.44 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[OGG1]] | -0.44 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[C1orf35]] | -0.44 | -0.22 / -0.37 | both halves | 6e-04 |  |
| [[TPRN]] | -0.44 | -0.10 / -0.44 | ⚠ not reproduced | 0.003 |  |
| [[LAT]] | -0.44 | -0.35 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEMP2]] | B | NEMP2 activity lowers NRK's level | lines that do not express NEMP2 (7) vs lines expressing it (43) | 2.38× higher at baseline in the lines without NEMP2 | 0.039 | ⚠ within organs, on part of the lines; also absent: EML6; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers NRK's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.558). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.0, 22.7); signed map (42.9, 22.7). **Vector** length 16.6, 4.81% of its response variance represented; |z| ≥ 3 in 113 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +9.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +4.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.4 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.8 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.7 | +1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.5 | +0.2 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.6 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.5 | -1.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.5 | -2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.4 | -1.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.4 | -1.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.4 | -0.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | Nik related kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.3 — chrX:105,822,539-105,958,610 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686A17109 |
| Gene groups (HGNC) | MAP4K family (GCK-IV subfamily) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z2Y5](https://www.uniprot.org/uniprotkb/Q7Z2Y5) (Nik-related protein kinase):

> May phosphorylate cofilin-1 and induce actin polymerization through this process, during the late stages of embryogenesis. Involved in the TNF-induced signaling pathway (By similarity).

**Summary**, from NCBI Gene [203447](https://www.ncbi.nlm.nih.gov/gene/203447):

> The mouse ortholog of this gene encodes a protein kinase required for JNK activation. The encoded protein may be involved in the induction of actin polymerization in late embryogenesis.[provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:25391](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25391) · Entrez [203447](https://www.ncbi.nlm.nih.gov/gene/203447) · UniProt [Q7Z2Y5](https://www.uniprot.org/uniprotkb/Q7Z2Y5) · Ensembl [ENSG00000123572](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123572)

## Data

Gene col 4444: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4444); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4444, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4444]; `tensor/DDL_lfc|DDL_z.npy` [4444]; `embed/gene_vectors.npy` [4444]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4444 or target_col == 4444). Every well: [[NRK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
