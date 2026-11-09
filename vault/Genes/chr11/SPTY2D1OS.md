---
symbol: "SPTY2D1OS"
type: "gene"
col: 14499
ensembl_id: "ENSG00000247595"
name: "mitochondrial sheath formation associated"
location: "11p15.1"
module: 23
arm: "+"
pooled_cpm: 7.67
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# SPTY2D1OS

*mitochondrial sheath formation associated* — 11p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.84× (z +11.3, q 6e-27, up in 29 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Niclosamide (olamine) (drug)]] 0.5 µM: 0.751× (z -3.8, q 0.094, down in 8 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Menadione (drug)]] 0.05 µM in 1 line (A-172 0.0948×); [[Harringtonine (drug)]] 0.05 µM in 1 line (RKO 0.105×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (BT-474 0.0851×).
> Its strongest partners by |cos| (80 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC32]] (+0.73, fdr 6e-05), [[MSTO1]] (+0.71, fdr 1e-05), [[CYB5D2]] (+0.71, fdr 1e-04); moves opposite to [[EFNA3]] (-0.62, fdr 8e-05), [[DHTKD1]] (-0.62, fdr 1e-04), [[EFNA4]] (-0.60, fdr 2e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MIR1915HG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14499.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.84×** | +11.3 | 6e-27 | 29/45 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.97×** | +8.9 | 2e-16 | 19/29 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.57×** | +8.4 | 1e-14 | 26/46 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +7.8 | 8e-13 | 9/15 (MIA PaCa-2, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +7.7 | 2e-12 | 28/45 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +7.5 | 7e-12 | 23/41 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +7.1 | 8e-11 | 14/21 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +6.5 | 7e-09 | 19/36 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +6.1 | 8e-08 | 20/46 (LoVo, A-172, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.0 | 4e-05 | 16/44 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.35×** | +4.0 | 0.004 | 10/42 (Hs 766T, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.34×** | +3.8 | 0.007 | 12/38 (C32, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.007 | 10/47 (HEC-1-A, A498, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.007 | 10/47 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.007 | 11/45 (KATO III, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.008 | 16/46 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.044 | 5/46 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14499.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Menadione (drug)]] 0.05 µM in 1 line (A-172 0.0948×); [[Harringtonine (drug)]] 0.05 µM in 1 line (RKO 0.105×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (BT-474 0.0851×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.751×** | -3.8 | 0.094 | 8/47 (PANC-1, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14499. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.52 | 0 | 2 (1 ⚠) | — | [[Menadione (drug)]] 0.05 µM 0.0948× (z -10.3) |
| [[BT-474 (line)]] | alt | 8.38 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0851× (z -9.5) |
| [[H4 (line)]] | wt | 9.57 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.05 µM 0.0804× (z -9.0) |
| [[HOP62 (line)]] | alt | 6.54 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +10.6) | — |
| [[HT-29 (line)]] | alt | 6.58 | 0 | 1 | — | [[vincristine (drug)]] 0.5 µM 0.0524× (z -8.6) |
| [[LoVo (line)]] | wt | 7.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 12.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +10.6) | — |
| [[RKO (line)]] | wt | 10.9 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.105× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 8.51 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.112× (z -9.1) ⚠ toxic |
| [[A-427 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14499), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 18 of them with an alert (⚠; 18 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC32]] | +0.73 | +0.73 / +0.39 | both halves | 6e-05 |  |
| [[MSTO1]] | +0.71 | +0.73 / +0.50 | both halves | 1e-05 |  |
| [[CYB5D2]] | +0.71 | +0.69 / +0.35 | both halves | 1e-04 |  |
| [[WARS2-AS1]] | +0.70 | +0.76 / +0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[OXA1L-DT]] | +0.68 | +0.67 / +0.35 | both halves | 1e-04 |  |
| [[TBCE-1]] | +0.68 | +0.64 / +0.31 | both halves | 2e-04 |  |
| [[PATL2]] | +0.68 | +0.71 / +0.27 | both halves | 3e-04 |  |
| [[RFX3-DT]] | +0.68 | +0.71 / +0.32 | both halves | 2e-04 |  |
| [[PPP1R3F]] | +0.67 | +0.67 / +0.26 | both halves | 3e-04 |  |
| [[IQCH-AS1]] | +0.67 | +0.71 / +0.29 | both halves | 2e-04 |  |
| [[CCDC90B-AS1]] | +0.67 | +0.74 / +0.10 | ⚠ one half (not replicated) | 0.003 |  |
| [[PPP1R12A-AS2]] | +0.67 | +0.72 / +0.27 | both halves | 3e-04 |  |
| [[ARRDC3-AS1]] | +0.67 | +0.70 / +0.29 | both halves | 3e-04 |  |
| [[KRBA2]] | +0.66 | +0.66 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFNA3]] | -0.62 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[DHTKD1]] | -0.62 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[EFNA4]] | -0.60 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[YIF1B]] | -0.60 | -0.58 / +0.02 | ⚠ one half (not replicated) | 1.00 |  |
| [[PIN1]] | -0.60 | -0.35 / -0.27 | both halves | 3e-04 |  |
| [[RAB3A]] | -0.59 | -0.39 / -0.13 | ⚠ not reproduced | 0.002 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR1915HG]] | B | MIR1915HG activity raises SPTY2D1OS's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 1.38× lower at baseline in the lines without MIR1915HG | 0.002 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SPTY2D1OS's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TMEM9B-AS1]] | B | TMEM9B-AS1 activity raises SPTY2D1OS's level | lines that do not express TMEM9B-AS1 (5) vs lines expressing it (45) | 1.54× lower at baseline in the lines without TMEM9B-AS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: TSEN2, SCML2, CAP2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.695). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (4.7, 18.2); signed map (31.4, -15.5). **Vector** length 54.7, 6.75% of its response variance represented; |z| ≥ 3 in 980 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.1 | +8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +7.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +6.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.2 | +2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +1.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.2 | +1.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | +2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -2.8 | +3.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -0.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | +2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | +1.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.2 | -1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -2.4 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial sheath formation associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.1 — chr11:18,588,781-18,610,255 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Kastor, Polluks, TSCL1; previously SPTY2D1-AS1, SPTY2D1OS |
| Matched by | ensembl_id |

**Function**, from UniProt [A0A0U1RRN3](https://www.uniprot.org/uniprotkb/A0A0U1RRN3) (Mitochondrial sheath formation-associated protein):

> [Isoform Kastor]: Regulates sperm development. May be involved in mitochondrial sheath formation.; [Isoform Polluks]: Regulates sperm development. May be involved in mitochondrial sheath formation.

**Summary**, from NCBI Gene [100506540](https://www.ncbi.nlm.nih.gov/gene/100506540):

> Predicted to be involved in sperm mitochondrial sheath assembly. Predicted to be located in mitochondrial outer membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:44122](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44122) · Entrez [100506540](https://www.ncbi.nlm.nih.gov/gene/100506540) · UniProt [A0A0U1RRN3](https://www.uniprot.org/uniprotkb/A0A0U1RRN3) · Ensembl [ENSG00000247595](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247595)

## Data

Gene col 14499: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14499); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14499, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14499]; `tensor/DDL_lfc|DDL_z.npy` [14499]; `embed/gene_vectors.npy` [14499]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14499 or target_col == 14499). Every well: [[SPTY2D1OS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPTY2D1OS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
