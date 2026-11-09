---
symbol: "MFSD2B"
type: "gene"
col: 12998
ensembl_id: "ENSG00000205639"
name: "MFSD2 lysolipid transporter B, sphingolipid"
location: "2p23.3"
module: 39
arm: "+"
pooled_cpm: 5.1
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# MFSD2B

*MFSD2 lysolipid transporter B, sphingolipid* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.10× (z +22.3, q 0e+00, up in 37 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.640× (z -5.0, q 3e-04, down in 14 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.457× (z -4.6, q 0.001, down in 9 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Hesperidin (drug)]] 0.5 µM in 1 line (C32 0.0698×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 0.213×; ⚠ toxic; transcription drop); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SW480 0.220×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02936]] (+0.82, fdr 7e-06), [[USP50]] (+0.81, fdr 7e-06), [[MYOCOS]] (+0.79, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[DYSF]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12998.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.10×** | +22.3 | 0e+00 | 37/37 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.59×** | +15.1 | 0e+00 | 28/38 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +8.0 | 2e-13 | 26/38 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.03×** | +7.9 | 4e-13 | 15/28 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +7.9 | 4e-13 | 6/9 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.86×** | +6.9 | 4e-10 | 21/39 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +6.4 | 1e-08 | 8/14 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +6.1 | 1e-07 | 19/35 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +6.0 | 1e-07 | 13/30 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +3.7 | 0.014 | 10/46 (A498, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.058 | 6/44 (Panc 03.27, COLO 205, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.062 | 9/44 (A-427, NCI-H23, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.096 | 2/44 (A498, NCI-H23) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pimozide (drug)]] 0.05 µM |  | 1.31× | +3.0 | 0.10 | 4/42 (SW48, SHP-77, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12998.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Hesperidin (drug)]] 0.5 µM in 1 line (C32 0.0698×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 0.213×; ⚠ toxic; transcription drop); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SW480 0.220×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.640×** | -5.0 | 3e-04 | 14/46 (SW48, HepG2/C3A, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.457×** | -4.6 | 0.001 | 9/42 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Erlotinib (drug)]] 5 µM |  | 0.726× | -3.4 | 0.11 | 11/43 (SW48, NCI-H2030, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.575× | -3.2 | 0.11 | 9/37 (HEC-1-A, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.736× | -3.2 | 0.11 | 11/43 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM |  | 0.576× | -3.2 | 0.11 | 3/34 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12998. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.76 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.41× (z +14.0) | — |
| [[HOP62 (line)]] | alt | 5.21 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 8.74× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 4.38 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +11.4) | — |
| [[SW480 (line)]] | alt | 5.57 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +10.6) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.220× (z -8.6) |
| [[A-172 (line)]] | wt | 6.01 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.11× (z +10.4) | — |
| [[A498 (line)]] | wt | 4.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.19× (z +10.8) | — |
| [[C32 (line)]] | wt | 6.12 | 0 | 1 | — | [[Hesperidin (drug)]] 0.5 µM 0.0698× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -8.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 4.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.00× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 6.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.71× (z +12.2) | — |
| [[NCI-H2030 (line)]] | alt | 11.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 5.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.34× (z +10.0) | — |
| [[A-427 (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12998), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02936]] | +0.82 | +0.82 / +0.74 | both halves | 7e-06 |  |
| [[USP50]] | +0.81 | +0.84 / +0.74 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.79 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[DRC1]] | +0.78 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[MCF2]] | +0.78 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[PLA2G12B]] | +0.77 | +0.79 / +0.62 | both halves | 7e-06 |  |
| [[L3MBTL2-AS1]] | +0.77 | +0.80 / +0.65 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.77 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[FAM151B]] | +0.77 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[ARL9]] | +0.75 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.75 | +0.80 / +0.64 | both halves | 7e-06 |  |
| [[XG]] | +0.75 | +0.71 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYSF]] | B | DYSF activity raises MFSD2B's level | lines that do not express DYSF (11) vs lines expressing it (39) | 1.34× lower at baseline in the lines without DYSF | 0.052 | ⚠ within organs, on part of the lines; also absent: ISM2, IRX3, DNAAF9; maybe low, not absent |
| [[SLC26A4]] | B | SLC26A4 activity raises MFSD2B's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.35× lower at baseline in the lines without SLC26A4 | 0.057 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers MFSD2B's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[EFNA2]] | B | EFNA2 activity raises MFSD2B's level | lines that do not express EFNA2 (8) vs lines expressing it (42) | 1.28× lower at baseline in the lines without EFNA2 | 0.073 | ⚠ within organs, on part of the lines; also absent: TFR2, USP43, BTG3-AS1; maybe low, not absent |
| [[ADORA1]] | B | ADORA1 activity raises MFSD2B's level | lines that do not express ADORA1 (7) vs lines expressing it (43) | 1.36× lower at baseline in the lines without ADORA1 | 0.089 | ⚠ within organs, on part of the lines; also absent: DRAM1, HHAT, SUGCT; maybe low, not absent |
| [[F2]] | B | F2 activity raises MFSD2B's level | lines that do not express F2 (11) vs lines expressing it (39) | 1.24× lower at baseline in the lines without F2 | 0.090 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ITGA2B]] | C | ITGA2B activity raises MFSD2B's level | lines that do not express ITGA2B (3) vs lines expressing it (47) | 1.53× lower at baseline in the lines without ITGA2B | 0.084 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PHC1, CFL2, HECTD2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.809). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.1, -14.4); signed map (18.3, 9.2). **Vector** length 72.4, 11.9% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +22.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.4 | +15.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +7.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +7.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +1.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | +0.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.0 | -4.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | +0.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.0 |
|  | [[NG25 (drug)]] 5 µM |  | -2.7 | -3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -1.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.9 | -3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -0.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | MFSD2 lysolipid transporter B, sphingolipid |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:24,010,081-24,063,321 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SLC59A2 |
| Gene groups (HGNC) | Solute carrier family 59 |
| Reactome | 3 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NFX1](https://www.uniprot.org/uniprotkb/A6NFX1) (Sphingosine-1-phosphate transporter MFSD2B):

> Lipid transporter that specifically mediates export of sphingosine-1-phosphate in red blood cells and platelets. Sphingosine-1-phosphate is a signaling sphingolipid and its export from red blood cells into in the plasma is required for red blood cell morphology (By similarity). Sphingosine-1-phosphate export from platelets is required for platelet aggregation and thrombus formation (By similarity). Mediates the export of different sphingosine-1-phosphate (S1P) species, including S1P(d18:0) …

**Summary**, from NCBI Gene [388931](https://www.ncbi.nlm.nih.gov/gene/388931):

> Predicted to enable symporter activity. Involved in lipid transport. Is active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:37207](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37207) · Entrez [388931](https://www.ncbi.nlm.nih.gov/gene/388931) · UniProt [A6NFX1](https://www.uniprot.org/uniprotkb/A6NFX1) · Ensembl [ENSG00000205639](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205639)

## Data

Gene col 12998: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12998); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12998, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12998]; `tensor/DDL_lfc|DDL_z.npy` [12998]; `embed/gene_vectors.npy` [12998]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12998 or target_col == 12998). Every well: [[MFSD2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFSD2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
