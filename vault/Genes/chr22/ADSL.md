---
symbol: "ADSL"
type: "gene"
col: 14218
ensembl_id: "ENSG00000239900"
name: "adenylosuccinate lyase"
location: "22q13.1"
module: 18
arm: "+"
pooled_cpm: 20.47
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# ADSL

*adenylosuccinate lyase* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.85× (z +13.5, q 1e-38, up in 33 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.20× (z +5.7, q 9e-07, up in 16 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.798× (z -5.0, q 3e-04, down in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.156×; ⚠ cell-cycle shift, explains ~4% of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (SW480 0.0866×; ⚠ toxic); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.341×; ⚠ cell-cycle shift, explains ~0% of this change); [[Pyridoxine (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.118×); [[Pimozide (drug)]] 0.05 µM in 1 line (HT-29 0.132×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW48 0.149×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAD]] (+0.70, fdr 7e-06), [[MYBBP1A]] (+0.69, fdr 7e-06), [[PUM3]] (+0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CLU]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14218.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +13.5 | 1e-38 | 33/42 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +12.2 | 1e-31 | 24/33 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +9.6 | 2e-19 | 23/39 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +7.0 | 5e-10 | 26/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.35×** | +6.5 | 8e-09 | 22/46 (SW480, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +6.1 | 8e-08 | 19/45 (HepG2/C3A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +5.7 | 9e-07 | 16/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.23×** | +4.5 | 4e-04 | 16/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +4.2 | 0.001 | 1/48 (COLO 205) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.20×** | +4.0 | 0.003 | 10/48 (A498, SNU-423, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.007 | 7/46 (PANC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.7 | 0.011 | 9/48 (NCI-H2347, NCI-H1792, …) | top dose only | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | 1.18× | +3.5 | 0.019 | 12/48 (C-33 A, LOX-IMVI, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.032 | 5/48 (SW480, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.17× | +3.3 | 0.033 | 8/48 (KATO III, LS 180, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.040 | 2/47 (NCI-H460, HOP62) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.040 | 5/47 (NCI-H460, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.040 | 7/47 (LOX-IMVI, HOP62, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.040 | 7/47 (LOX-IMVI, SNU-423, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 5 µM |  | 1.11× | +3.1 | 0.047 | 2/48 (NCI-H1573, SK-MEL-2) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.051 | 6/46 (A-172, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.15× | +2.9 | 0.083 | 9/45 (Hs 766T, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14218.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.156×; ⚠ cell-cycle shift, explains ~4% of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (SW480 0.0866×; ⚠ toxic); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.341×; ⚠ cell-cycle shift, explains ~0% of this change); [[Pyridoxine (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.118×); [[Pimozide (drug)]] 0.05 µM in 1 line (HT-29 0.132×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW48 0.149×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.798×** | -5.0 | 3e-04 | 16/48 (SW48, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | 0.899× | -3.4 | 0.16 | 3/48 (MIA PaCa-2, HCT15, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.864× | -3.3 | 0.16 | 15/47 (SW 900, A-172, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 0.5 µM |  | 0.865× | -3.2 | 0.16 | 4/48 (NCI-H2347, SW 1088, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.872× | -3.1 | 0.24 | 9/47 (AsPC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14218. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 30.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.38× (z +8.7) ⚠ toxic; transcription drop | [[Lonafarnib (drug)]] 5 µM 0.0866× (z -13.4) ⚠ toxic |
| [[A-427 (line)]] | wt | 22.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -14.8) ⚠ cell-cycle shift, explains ~4% of this change |
| [[NCI-H460 (line)]] | wt | 18.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +11.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 19.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.71× (z +8.5) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 27.2 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0771× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 20.8 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.118× (z -11.9) |
| [[HT-29 (line)]] | alt | 10.3 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.132× (z -10.4) |
| [[KATO III (line)]] | alt | 15.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.24× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 25.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 18.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -9.1) |
| [[A-172 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14218), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAD]] | +0.70 | +0.59 / +0.71 | both halves | 7e-06 | pathway: Metabolism of nucleotides; STRING 680 |
| [[MYBBP1A]] | +0.69 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[PUM3]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[IPO4]] | +0.68 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[TRAP1]] | +0.67 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[URB1]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[HEATR1]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[PFAS]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 | same gene group; pathway: Metabolism of nucleotides; STRING 847 |
| [[MRPL3]] | +0.64 | +0.50 / +0.67 | both halves | 1e-05 | STRING 458 |
| [[BOP1]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[MTG1]] | +0.63 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[PDCD11]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLU]] | B | CLU activity raises ADSL's level | lines that do not express CLU (11) vs lines expressing it (39) | 1.49× lower at baseline in the lines without CLU | 0.014 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ATP1B1]] | B | ATP1B1 activity lowers ADSL's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 1.46× higher at baseline in the lines without ATP1B1 | 0.045 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.530). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-12.2, -36.7); signed map (-5.3, -47.2). **Vector** length 59.5, 8.50% of its response variance represented; |z| ≥ 3 in 753 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +13.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +12.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +3.5 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.6 | +3.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -2.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.6 | -1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | adenylosuccinate lyase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:40,346,461-40,390,463 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Purinosome; Carbon-nitrogen lyases |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Reactome | 3 pathways, smallest: Purine ribonucleoside monophosphate biosynthesis; Nucleotide biosynthesis; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [P30566](https://www.uniprot.org/uniprotkb/P30566) (Adenylosuccinate lyase):

> Catalyzes two non-sequential steps in de novo AMP synthesis: converts (S)-2-(5-amino-1-(5-phospho-D-ribosyl)imidazole-4-carboxamido)succinate (SAICAR) to fumarate plus 5-amino-1-(5-phospho-D-ribosyl)imidazole-4-carboxamide, and thereby also contributes to de novo IMP synthesis, and converts succinyladenosine monophosphate (SAMP) to AMP and fumarate.

**Summary**, from NCBI Gene [158](https://www.ncbi.nlm.nih.gov/gene/158):

> The protein encoded by this gene belongs to the lyase 1 family. It is an essential enzyme involved in purine metabolism, and catalyzes two non-sequential reactions in the de novo purine biosynthetic pathway: the conversion of succinylaminoimidazole carboxamide ribotide (SAICAR) to aminoimidazole carboxamide ribotide (AICAR) and the conversion of adenylosuccinate (S-AMP) to adenosine monophosphate (AMP). Mutations in this gene are associated with adenylosuccinase deficiency (ADSLD), a disorder …

**Accessions** — [HGNC:291](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:291) · Entrez [158](https://www.ncbi.nlm.nih.gov/gene/158) · UniProt [P30566](https://www.uniprot.org/uniprotkb/P30566) · Ensembl [ENSG00000239900](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000239900)

## Data

Gene col 14218: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14218); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14218, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14218]; `tensor/DDL_lfc|DDL_z.npy` [14218]; `embed/gene_vectors.npy` [14218]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14218 or target_col == 14218). Every well: [[ADSL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADSL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
