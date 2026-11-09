---
symbol: "ARHGAP15"
type: "gene"
col: 1135
ensembl_id: "ENSG00000075884"
name: "Rho GTPase activating protein 15"
location: "2q22.2-q22.3"
module: 26
arm: "+"
pooled_cpm: 4.19
n_lines_expressing: 47
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# ARHGAP15

*Rho GTPase activating protein 15* — 2q22.2-q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.95× (z +24.8, q 0e+00, up in 30 of 32 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (A549 0.0354×, NCI-H1792 0.0564×; ⚠ toxic); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0259×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYNPO2]] (+0.76, fdr 7e-06), [[LINC02268]] (+0.76, fdr 7e-06), [[NEB]] (+0.75, fdr 1e-05); moves opposite to [[ACTR5]] (-0.68, fdr 2e-05), [[FAM118A]] (-0.65, fdr 3e-05), [[NBPF3]] (-0.62, fdr 1e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1135.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.95×** | +24.8 | 0e+00 | 30/32 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.81×** | +17.1 | 0e+00 | 28/33 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.95×** | +12.4 | 4e-33 | 25/31 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.81×** | +12.1 | 2e-31 | 30/38 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.51×** | +10.5 | 1e-23 | 4/10 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.16×** | +9.8 | 9e-21 | 16/41 (A498, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.51×** | +8.0 | 1e-13 | 1/8 (NCI-H2030) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.50×** | +7.9 | 1e-13 | 13/26 (NCI-H460, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.23×** | +7.2 | 3e-11 | 1/13 (HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.09×** | +6.4 | 9e-09 | 13/31 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.85×** | +5.2 | 9e-06 | 12/35 (A549, A498, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +4.7 | 1e-04 | 11/41 (A-427, HEC-1-A, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.30×** | +3.9 | 0.004 | 2/8 (NCI-H460, A498) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.007 | 5/40 (NCI-H1792, RPMI-7951, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +3.7 | 0.007 | 8/35 (NCI-H661, A-427, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.65×** | +3.2 | 0.046 | 1/24 (RPMI-7951) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.050 | 11/36 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +3.0 | 0.075 | 4/33 (RPMI-7951, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.60×** | +3.0 | 0.075 | 0/25 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1135.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (A549 0.0354×, NCI-H1792 0.0564×; ⚠ toxic); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0259×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.667× | -3.7 | 0.13 | 9/40 (NCI-H2030, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.680× | -3.5 | 0.13 | 13/40 (NCI-H2030, LOX-IMVI, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.711× | -3.1 | 0.30 | 7/41 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.714× | -3.1 | 0.30 | 10/39 (H4, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1135. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.8× (z +21.7) | — |
| [[NCI-H1792 (line)]] | alt | 12.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 19.5× (z +15.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0564× (z -10.0) ⚠ toxic |
| [[A498 (line)]] | wt | 7.37 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 43.2× (z +13.2) | — |
| [[A549 (line)]] | wt | 9.84 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0354× (z -11.0) ⚠ toxic |
| [[C32 (line)]] | wt | 4.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +8.8) | — |
| [[HEC-1-A (line)]] | alt | 1.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 4.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.6× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 2.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.8× (z +11.0) | — |
| [[Hs 766T (line)]] | wt | 1.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.1× (z +10.1) | — |
| [[hTERT-HPNE (line)]] | wt | 2.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.2× (z +9.1) | — |
| [[LoVo (line)]] | wt | 1.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.4× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 11.5 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0259× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 6.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.6× (z +11.2) | — |
| [[SNU-423 (line)]] | alt | 4.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +10.9) | — |
| [[SW480 (line)]] | alt | 1.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +9.5) | — |
| [[A-172 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.955 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.938 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1135), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYNPO2]] | +0.76 | +0.78 / +0.58 | both halves | 7e-06 |  |
| [[LINC02268]] | +0.76 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[NEB]] | +0.75 | +0.79 / +0.49 | both halves | 1e-05 |  |
| [[CFAP54]] | +0.74 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.73 | +0.73 / +0.46 | both halves | 3e-05 |  |
| [[CIBAR1-DT]] | +0.72 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[LRRN3]] | +0.72 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[PPP1R12A-AS2]] | +0.72 | +0.76 / +0.39 | both halves | 5e-05 |  |
| [[CCDC90B-AS1]] | +0.71 | +0.73 / +0.43 | both halves | 3e-05 |  |
| [[CACNA2D1]] | +0.71 | +0.73 / +0.37 | both halves | 8e-05 |  |
| [[COL24A1]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[EYS]] | +0.71 | +0.73 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTR5]] | -0.68 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[FAM118A]] | -0.65 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[NBPF3]] | -0.62 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[PLA2G12A]] | -0.62 | -0.54 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ARHGAP15's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MOCS1]] | B | MOCS1 activity lowers ARHGAP15's level | lines that do not express MOCS1 (13) vs lines expressing it (36) | 1.01× higher at baseline in the lines without MOCS1 | 0.086 | ⚠ within organs, on part of the lines; also absent: SNRPN, MYH10, ANKRD6 |
| [[RMDN2-AS1]] | B | RMDN2-AS1 activity raises ARHGAP15's level | lines that do not express RMDN2-AS1 (14) vs lines expressing it (36) | 1.16× lower at baseline in the lines without RMDN2-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: EHD3, PLOD2, ZNF43; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.719). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (24.8, 24.1); signed map (37.1, 14.0). **Vector** length 68.5, 12.2% of its response variance represented; |z| ≥ 3 in 1,011 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.6 | +24.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.1 | +17.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.4 | +12.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +5.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +1.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -3.4 | -3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -2.7 | -3.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -3.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q22.2-q22.3 — chr2:143,091,362-143,768,352 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BM046 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Rho GTPase activating proteins |
| Reactome | 5 pathways, smallest: RAC3 GTPase cycle; RAC1 GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53QZ3](https://www.uniprot.org/uniprotkb/Q53QZ3) (Rho GTPase-activating protein 15):

> GTPase activator for the Rho-type GTPases by converting them to an inactive GDP-bound state. Has activity toward RAC1. Overexpression results in an increase in actin stress fibers and cell contraction.

**Summary**, from NCBI Gene [55843](https://www.ncbi.nlm.nih.gov/gene/55843):

> RHO GTPases (see ARHA; MIM 165390) regulate diverse biologic processes, and their activity is regulated by RHO GTPase-activating proteins (GAPs), such as ARHGAP15 (Seoh et al., 2003 [PubMed 12650940]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:21030](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21030) · Entrez [55843](https://www.ncbi.nlm.nih.gov/gene/55843) · UniProt [Q53QZ3](https://www.uniprot.org/uniprotkb/Q53QZ3) · Ensembl [ENSG00000075884](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075884)

## Data

Gene col 1135: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1135); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1135, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1135]; `tensor/DDL_lfc|DDL_z.npy` [1135]; `embed/gene_vectors.npy` [1135]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1135 or target_col == 1135). Every well: [[ARHGAP15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
