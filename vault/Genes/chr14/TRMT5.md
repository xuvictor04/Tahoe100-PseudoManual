---
symbol: "TRMT5"
type: "gene"
col: 4770
ensembl_id: "ENSG00000126814"
name: "tRNA methyltransferase 5"
location: "14q23.1"
module: 7
arm: "+"
pooled_cpm: 9.75
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# TRMT5

*tRNA methyltransferase 5* — 14q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.80× (z +13.4, q 2e-38, up in 31 of 36 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.32× (z +11.4, q 2e-27, up in 36 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[PF-06260933 (drug)]] 5 µM: 0.566× (z -4.1, q 0.026, down in 18 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (Hs 766T 0.0989×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.118×; ⚠ cell-cycle shift, explains ~42% of this change); [[Pimozide (drug)]] 0.5 µM in 1 line (C-33 A 0.101×; ⚠ transcription drop); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (A-427 0.134×); [[Estrone sulfate (potassium) (drug)]] 0.05 µM in 1 line (COLO 205 0.0694×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KICS2]] (+0.81, fdr 7e-06), [[ZNF507]] (+0.80, fdr 7e-06), [[NOL11]] (+0.77, fdr 7e-06); moves opposite to [[CBFA2T2]] (-0.68, fdr 1e-05), [[PHF1]] (-0.67, fdr 1e-05), [[SEC11A]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CYP46A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4770.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.80×** | +13.4 | 2e-38 | 31/36 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.32×** | +11.4 | 2e-27 | 36/43 (NCI-H1792, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.15×** | +10.3 | 9e-23 | 37/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.12×** | +9.8 | 2e-20 | 33/46 (NCI-H1573, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +6.9 | 8e-10 | 25/47 (NCI-H1573, H4, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.7 | 2e-09 | 25/44 (NCI-H1792, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.61×** | +6.4 | 1e-08 | 27/46 (NCI-H2347, LoVo, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +5.6 | 1e-06 | 19/48 (C32, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.3 | 6e-06 | 24/48 (CFPAC-1, NCI-H2030, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +4.5 | 4e-04 | 12/47 (CFPAC-1, C32, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +4.3 | 0.001 | 11/26 (NCI-H1573, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +4.1 | 0.002 | 13/38 (NCI-H460, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +3.8 | 0.007 | 9/47 (CFPAC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.31×** | +3.6 | 0.011 | 15/36 (NCI-H1573, SW 900, …) | inconsistent across doses | composition shift |
| [[Megestrol (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.016 | 9/48 (LS 180, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.051 | 8/45 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.0 | 0.088 | 10/43 (RPMI-7951, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.088 | 8/45 (NCI-H1573, HEC-1-A, …) | top dose only |  |
| [[Busulfan (drug)]] 5 µM |  | 1.17× | +3.0 | 0.091 | 7/48 (SW48, A-427, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4770.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (Hs 766T 0.0989×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.118×; ⚠ cell-cycle shift, explains ~42% of this change); [[Pimozide (drug)]] 0.5 µM in 1 line (C-33 A 0.101×; ⚠ transcription drop); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (A-427 0.134×); [[Estrone sulfate (potassium) (drug)]] 0.05 µM in 1 line (COLO 205 0.0694×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PF-06260933 (drug)]] 5 µM |  | **0.566×** | -4.1 | 0.026 | 18/45 (MIA PaCa-2, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.836× | -3.5 | 0.12 | 11/48 (LS 180, RKO, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | 0.801× | -3.1 | 0.38 | 10/43 (LOX-IMVI, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4770. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 8.65 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 10.3× (z +11.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.69× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 9.34 | 0 | 2 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0907× (z -9.5) ⚠ toxic · without an alert: [[Hydroxyurea (drug)]] 0.05 µM 0.101× (z -8.7) |
| [[A-427 (line)]] | wt | 10.5 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.134× (z -10.6) |
| [[BT-474 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.118× (z -10.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[C-33 A (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.101× (z -10.6) ⚠ transcription drop |
| [[COLO 205 (line)]] | alt | 6.15 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.05 µM 0.0694× (z -9.4) |
| [[Hs 766T (line)]] | wt | 8.77 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0989× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H2030 (line)]] | alt | 11.3 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.05× (z +8.7) ⚠ toxic | — |
| [[NCI-H2347 (line)]] | alt | 8.75 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.110× (z -8.8) ⚠ toxic |
| [[SW480 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4770), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KICS2]] | +0.81 | +0.84 / +0.66 | both halves | 7e-06 |  |
| [[ZNF507]] | +0.80 | +0.84 / +0.67 | both halves | 7e-06 |  |
| [[NOL11]] | +0.77 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[DDX20]] | +0.76 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[ZXDB]] | +0.76 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[UTP15]] | +0.72 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[ZNF614]] | +0.72 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[ARL14EP]] | +0.72 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[ZNF816]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[RPL7L1]] | +0.71 | +0.78 / +0.60 | both halves | 7e-06 |  |
| [[UMPS]] | +0.70 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[ADO]] | +0.69 | +0.67 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBFA2T2]] | -0.68 | -0.70 / -0.57 | both halves | 1e-05 |  |
| [[PHF1]] | -0.67 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[SEC11A]] | -0.66 | -0.69 / -0.53 | both halves | 1e-05 |  |
| [[GTF2IP4]] | -0.65 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[ADIPOR1]] | -0.65 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[SEZ6L2]] | -0.65 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[TMEM41B]] | -0.64 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[PDZD7]] | -0.64 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[GNAI2]] | -0.63 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[RAB40C]] | -0.62 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.62 | -0.63 / -0.40 | both halves | 5e-05 |  |
| [[TM9SF2]] | -0.62 | -0.66 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP46A1]] | B | CYP46A1 activity raises TRMT5's level | lines that do not express CYP46A1 (6) vs lines expressing it (44) | 1.48× lower at baseline in the lines without CYP46A1 | 0.038 | ⚠ within organs, on part of the lines; also absent: CCDC102A, TPST1, DZIP1L; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.655). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-35.5, 13.1); signed map (2.7, -37.1). **Vector** length 82.6, 15.1% of its response variance represented; |z| ≥ 3 in 948 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.1 | +10.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +11.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.6 | +6.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.7 | +9.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.6 | +13.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +5.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +0.7 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -0.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.2 | -1.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -3.1 | +3.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | +0.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.7 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | tRNA methyltransferase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.1 — chr14:60,971,441-60,981,170 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRM5; previously KIAA1393 |
| Gene groups (HGNC) | 7BS DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Reactome | 4 pathways, smallest: Synthesis of wybutosine at G37 of tRNA(Phe); tRNA modification in the nucleus and cytosol; tRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q32P41](https://www.uniprot.org/uniprotkb/Q32P41) (tRNA):

> Involved in mitochondrial tRNA methylation. Specifically methylates the N1 position of guanosine-37 in various tRNAs. Methylation is not dependent on the nature of the nucleoside 5' of the target nucleoside. This is the first step in the biosynthesis of wybutosine (yW), a modified base adjacent to the anticodon of tRNAs and required for accurate decoding.

**Summary**, from NCBI Gene [57570](https://www.ncbi.nlm.nih.gov/gene/57570):

> tRNAs contain as many as 13 or 14 nucleotides that are modified posttranscriptionally by enzymes that are highly specific for particular nucleotides in the tRNA structure. TRMT5 methylates the N1 position of guanosine-37 (G37) in selected tRNAs using S-adenosyl methionine (Brule et al., 2004 [PubMed 15248782]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:23141](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23141) · Entrez [57570](https://www.ncbi.nlm.nih.gov/gene/57570) · UniProt [Q32P41](https://www.uniprot.org/uniprotkb/Q32P41) · Ensembl [ENSG00000126814](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126814)

## Data

Gene col 4770: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4770); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4770, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4770]; `tensor/DDL_lfc|DDL_z.npy` [4770]; `embed/gene_vectors.npy` [4770]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4770 or target_col == 4770). Every well: [[TRMT5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRMT5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
