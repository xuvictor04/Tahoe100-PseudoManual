---
symbol: "DTD2"
type: "gene"
col: 4978
ensembl_id: "ENSG00000129480"
name: "D-aminoacyl-tRNA deacylase 2"
location: "14q12"
module: 18
arm: "+"
pooled_cpm: 7.52
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 15
n_dd_up_clean: 14
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# DTD2

*D-aminoacyl-tRNA deacylase 2* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.00× (z +17.5, q 0e+00, up in 28 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.53× (z +9.6, q 1e-19, up in 20 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.566× (z -12.8, q 1e-34, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIOX2]] (+0.73, fdr 7e-06), [[ADAT2]] (+0.72, fdr 7e-06), [[NAE1]] (+0.72, fdr 7e-06); moves opposite to [[MTHFR]] (-0.59, fdr 3e-05), [[PDPK1]] (-0.54, fdr 1e-04), [[OTUD5]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DUXAP8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4978.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.00×** | +17.5 | 0e+00 | 28/29 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.77×** | +15.6 | 0e+00 | 15/15 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.37×** | +12.7 | 7e-35 | 15/19 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +11.3 | 2e-27 | 23/31 (SW1417, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.53×** | +9.6 | 1e-19 | 20/47 (NCI-H2347, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.58×** | +7.1 | 2e-10 | 19/46 (NCI-H2030, NCI-H1573, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.9 | 4e-07 | 13/42 (NCI-H2030, NCI-H23, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.25×** | +5.0 | 5e-05 | 15/45 (LS 180, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.40×** | +4.8 | 1e-04 | 10/47 (NCI-H1573, BT-474, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +4.7 | 1e-04 | 13/36 (NCI-H23, BT-474, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.34×** | +4.7 | 1e-04 | 13/47 (NCI-H1573, A-172, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.72×** | +4.5 | 3e-04 | 10/36 (NCI-H460, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +4.5 | 3e-04 | 12/47 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.004 | 7/47 (HepG2/C3A, NCI-H1792, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +3.9 | 0.004 | 6/47 (SNU-423, COLO 205, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.56×** | +3.7 | 0.007 | 2/42 (A-427, CFPAC-1) | inconsistent across doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.007 | 5/47 (A549, HOP62, …) | top dose only |  |
| [[Monocrotaline (drug)]] 0.05 µM |  | **1.28×** | +3.6 | 0.008 | 7/42 (PANC-1, RKO, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.012 | 9/43 (SW480, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.52×** | +3.5 | 0.013 | 1/42 (NCI-H1573) | top dose only | noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.015 | 5/33 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **1.29×** | +2.9 | 0.066 | 3/43 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.20×** | +2.9 | 0.067 | 4/46 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +2.8 | 0.085 | 2/46 (H4, HT-29) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4978.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.566×** | -12.8 | 1e-34 | 32/45 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.357×** | -8.6 | 3e-15 | 24/46 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.428×** | -7.1 | 3e-10 | 22/43 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.902× | -5.3 | 2e-05 | 10/48 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.732×** | -5.0 | 8e-05 | 16/44 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.553×** | -4.9 | 8e-05 | 17/39 (NCI-H2347, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.765×** | -4.2 | 0.002 | 8/46 (AsPC-1, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Cytarabine (drug)]] 5 µM |  | **0.758×** | -4.2 | 0.002 | 9/46 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Malotilate (drug)]] 0.05 µM |  | **0.774×** | -4.1 | 0.003 | 10/46 (AN3 CA, SK-MEL-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.776×** | -3.9 | 0.006 | 12/46 (PANC-1, A498, …) | top dose only | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.776×** | -3.5 | 0.021 | 10/46 (SNU-1, SW48, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[SBI-0640756 (drug)]] 5 µM |  | **0.659×** | -3.5 | 0.026 | 9/37 (SW480, C32, …) | top dose only | noisy plate (z scaled) |
| [[Roxadustat (drug)]] 5 µM |  | **0.806×** | -3.3 | 0.044 | 9/46 (COLO 205, HepG2/C3A, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **0.805×** | -3.2 | 0.059 | 11/38 (LOX-IMVI, HOP62, …) | inconsistent across doses |  |
| [[Indacaterol (maleate) (drug)]] 0.05 µM |  | **0.823×** | -3.1 | 0.078 | 5/47 (CHP-212, SW 1271, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.816×** | -3.0 | 0.084 | 9/45 (SW480, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4978. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 10.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.7× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 9.79 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -16.0) |
| [[PANC-1 (line)]] | alt | 9.32 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -14.6) |
| [[SW480 (line)]] | alt | 9.26 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.236× (z -9.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0674× (z -12.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 4.93 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -9.0) |
| [[LoVo (line)]] | wt | 8.63 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 5.51 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -14.0) |
| [[NCI-H23 (line)]] | alt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -12.0) |
| [[SHP-77 (line)]] | alt | 10.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -9.3) |
| [[A-172 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4978), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIOX2]] | +0.73 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[ADAT2]] | +0.72 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[NAE1]] | +0.72 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[SFXN4]] | +0.71 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[EEF1E1]] | +0.70 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[RFT1]] | +0.68 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[HEATR1]] | +0.68 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[CAD]] | +0.67 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[WDR12]] | +0.67 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[MRPL3]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[MDN1]] | +0.66 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[TSEN2]] | +0.66 | +0.75 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTHFR]] | -0.59 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[PDPK1]] | -0.54 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[OTUD5]] | -0.54 | -0.57 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUXAP8]] | B | DUXAP8 activity raises DTD2's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.83× lower at baseline in the lines without DUXAP8 | 0.014 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.772). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-9.9, -37.5); signed map (-4.1, -52.0). **Vector** length 66.2, 10.6% of its response variance represented; |z| ≥ 3 in 867 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.55 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.9 | +9.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +11.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +7.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.5 | +4.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +3.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.0 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +1.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.7 | +3.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | -12.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.2 | -8.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -4.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -2.4 | -3.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | +0.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -7.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.3 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | D-aminoacyl-tRNA deacylase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:31,446,036-31,457,506 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC9912; previously C14orf126 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FN9](https://www.uniprot.org/uniprotkb/Q96FN9) (D-aminoacyl-tRNA deacylase 2):

> Deacylates mischarged D-aminoacyl-tRNAs (By similarity). Also deacylates mischarged glycyl-tRNA(Ala), protecting cells against glycine mischarging by AlaRS (By similarity). Probably acts by rejecting L-amino acids from its binding site rather than specific recognition of D-amino acids (By similarity). Catalyzes the hydrolysis of D-tyrosyl-tRNA(Tyr), has no activity on correctly charged L-tyrosyl-tRNA(Tyr) (By similarity). By recycling D-aminoacyl-tRNA to D-amino acids and free tRNA molecules, …

**Summary**, from NCBI Gene [112487](https://www.ncbi.nlm.nih.gov/gene/112487):

> Enables Ala-tRNA(Thr) deacylase activity. Involved in aminoacyl-tRNA metabolism involved in translational fidelity. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20277](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20277) · Entrez [112487](https://www.ncbi.nlm.nih.gov/gene/112487) · UniProt [Q96FN9](https://www.uniprot.org/uniprotkb/Q96FN9) · Ensembl [ENSG00000129480](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129480)

## Data

Gene col 4978: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4978); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4978, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4978]; `tensor/DDL_lfc|DDL_z.npy` [4978]; `embed/gene_vectors.npy` [4978]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4978 or target_col == 4978). Every well: [[DTD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DTD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
