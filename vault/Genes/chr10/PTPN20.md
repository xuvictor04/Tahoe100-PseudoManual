---
symbol: "PTPN20"
type: "gene"
col: 12827
ensembl_id: "ENSG00000204179"
name: "protein tyrosine phosphatase non-receptor type 20"
location: "10q11.22"
module: 19
arm: "+"
pooled_cpm: 2.1
n_lines_expressing: 22
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# PTPN20

*protein tyrosine phosphatase non-receptor type 20* — 10q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.22× (z +12.2, q 1e-31, up in 1 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM: 2.04× (z +5.0, q 7e-05, up in 0 of 12 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.161×, NCI-H460 0.255×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (PANC-1 0.262×, MIA PaCa-2 0.209×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 0.186×; ⚠ toxic; transcription drop); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (CFPAC-1 0.104×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFP69]] (+0.64, fdr 6e-05), [[CHST10]] (+0.63, fdr 1e-05), [[F2RL2]] (+0.58, fdr 1e-05); moves opposite to [[OXR1-AS1]] (-0.46, fdr 4e-04), [[AP4M1]] (-0.44, fdr 4e-05), [[ZNHIT1]] (-0.43, fdr 2e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CNNM1]] → it (grade C ⚠); 3 go from it, the strongest it → [[ZNF239]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12827.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.22×** | +12.2 | 1e-31 | 1/4 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.65×** | +9.0 | 5e-17 | 2/11 (NCI-H2030, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.08×** | +8.1 | 2e-13 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **4.00×** | +6.9 | 8e-10 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +5.3 | 1e-05 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **2.04×** | +5.0 | 7e-05 | 0/12 | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.05×** | +4.8 | 1e-04 | 2/8 (HEC-1-A, CFPAC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.62×** | +4.7 | 1e-04 | 2/18 (A549, NCI-H2030) | top dose only | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.96×** | +4.7 | 2e-04 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.52×** | +4.6 | 2e-04 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.86×** | +4.3 | 8e-04 | 0/9 | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +4.2 | 0.001 | 0/15 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.48×** | +3.9 | 0.005 | 0/13 | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.007 | 1/18 (NCI-H460) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +3.7 | 0.008 | 0/12 | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.62×** | +3.4 | 0.023 | 1/11 (A549) | inconsistent across doses |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.59×** | +3.2 | 0.034 | 0/12 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.70×** | +3.0 | 0.061 | 0/11 | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.67×** | +2.9 | 0.081 | 0/12 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.161×, NCI-H460 0.255×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (PANC-1 0.262×, MIA PaCa-2 0.209×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 0.186×; ⚠ toxic; transcription drop); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (CFPAC-1 0.104×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12827. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.93 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.142× (z -9.0) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.255× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 11.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -11.8) |
| [[PANC-1 (line)]] | alt | 7.95 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 4.68 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.104× (z -8.9) |
| [[A-172 (line)]] | wt | 0.157 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.117 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.129 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.212 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.149 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.183 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.143 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.173 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.148 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.152 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.154 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.146 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.179 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.202 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.152 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.147 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.168 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.140 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.142 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.814 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 0.696 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.931 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.135 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.161 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.117 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.846 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.240 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.196 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.234 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12827), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFP69]] | +0.64 | +0.68 / +0.38 | both halves | 6e-05 |  |
| [[CHST10]] | +0.63 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[F2RL2]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[ESYT3]] | +0.58 | +0.60 / +0.32 | both halves | 1e-04 |  |
| [[RNF182]] | +0.56 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[TMEM177]] | +0.55 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[TSPYL5]] | +0.55 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[SLC46A1]] | +0.54 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[NCKAP5-AS2]] | +0.53 | +0.55 / +0.31 | both halves | 2e-04 |  |
| [[SEC14L4]] | +0.53 | +0.49 / +0.38 | both halves | 7e-05 |  |
| [[LRRC63]] | +0.51 | +0.57 / +0.32 | both halves | 1e-04 |  |
| [[ZNF30]] | +0.51 | +0.49 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OXR1-AS1]] | -0.46 | -0.26 / -0.46 | both halves | 4e-04 |  |
| [[AP4M1]] | -0.44 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[ZNHIT1]] | -0.43 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[PPP1R15B-AS1]] | -0.43 | -0.22 / -0.40 | both halves | 6e-04 |  |
| [[EFCAB6]] | -0.43 | -0.21 / -0.47 | both halves | 7e-04 |  |
| [[TSEN34]] | -0.43 | -0.37 / -0.55 | both halves | 9e-05 |  |
| [[RNASEK]] | -0.43 | -0.32 / -0.35 | both halves | 1e-04 |  |
| [[TSPOAP1-AS1]] | -0.42 | -0.25 / -0.43 | both halves | 4e-04 |  |
| [[UPF2]] | -0.42 | -0.30 / -0.42 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNNM1]] | C | CNNM1 activity raises PTPN20's level | lines that do not express CNNM1 (24) vs lines expressing it (26) | 1.69× lower at baseline in the lines without CNNM1 | 0.048 | ⚠ within organs, on part of the lines; also absent: GAL, SLC35F3, RHCG; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF239]] | B | PTPN20 activity raises ZNF239's level | lines that do not express PTPN20 (28) vs lines expressing it (22) | 1.47× lower at baseline in the lines without PTPN20 | 0.078 | ⚠ within organs, on part of the lines; also absent: TSPYL5, ENSG00000234426, GPR141 |
| [[CAMK1]] | B | PTPN20 activity raises CAMK1's level | lines that do not express PTPN20 (28) vs lines expressing it (22) | 1.54× lower at baseline in the lines without PTPN20 | 0.079 | ⚠ within organs, on part of the lines; also absent: TSPYL5, ENSG00000234426, GPR141 |
| [[TSEN34]] | B | PTPN20 activity raises TSEN34's level | lines that do not express PTPN20 (28) vs lines expressing it (22) | 1.09× lower at baseline in the lines without PTPN20 | 0.098 | ⚠ within organs, on part of the lines; also absent: TSPYL5, ENSG00000234426, GPR141 |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.419). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.2, 23.4); signed map (21.6, 26.6). **Vector** length 29.3, 5.25% of its response variance represented; |z| ≥ 3 in 394 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +12.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.6 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.5 | +9.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.4 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +0.8 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.7 | +1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +0.7 | -0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.7 | +0.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.6 | +4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | +0.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -0.9 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.6 | +2.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.5 | -1.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -0.5 | -0.7 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -0.5 | -0.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.5 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase non-receptor type 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.22 — chr10:46,911,396-47,002,488 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA42B19.1, DKFZP566K0524, bA142I17.1, CT126; previously PTPN20A, PTPN20B |
| Gene groups (HGNC) | Protein tyrosine phosphatases non-receptor type |
| Reactome | 4 pathways, smallest: Interleukin-37 signaling; Interleukin-1 family signaling; Signaling by Interleukins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4JDL3](https://www.uniprot.org/uniprotkb/Q4JDL3) (Tyrosine-protein phosphatase non-receptor type 20):

> Tyrosine-protein phosphatase targeted to sites of actin polymerization in response of varied extracellular stimuli. Has tyrosine phosphatase activity towards various tyrosyl phosphorylated substrates.

**Summary**, from NCBI Gene [26095](https://www.ncbi.nlm.nih.gov/gene/26095):

> The product of this gene belongs to the family of classical tyrosine-specific protein tyrosine phosphatases. Many protein tyrosine phosphatases have been shown to regulate fundamental cellular processes. The encoded protein appears to be targeted to sites of actin polymerization. A pseudogene of this gene has been defined on chromosome 10. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2014]

**Accessions** — [HGNC:23423](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23423) · Entrez [26095](https://www.ncbi.nlm.nih.gov/gene/26095) · UniProt [Q4JDL3](https://www.uniprot.org/uniprotkb/Q4JDL3) · Ensembl [ENSG00000204179](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204179)

## Data

Gene col 12827: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12827); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12827, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12827]; `tensor/DDL_lfc|DDL_z.npy` [12827]; `embed/gene_vectors.npy` [12827]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12827 or target_col == 12827). Every well: [[PTPN20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPN20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
