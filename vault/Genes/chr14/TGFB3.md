---
symbol: "TGFB3"
type: "gene"
col: 4103
ensembl_id: "ENSG00000119699"
name: "transforming growth factor beta 3"
location: "14q24.3"
module: 35
arm: "+"
pooled_cpm: 3.16
n_lines_expressing: 48
n_dd_up: 14
n_dd_down: 18
n_dd_up_clean: 10
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# TGFB3

*transforming growth factor beta 3* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.61× (z +25.3, q 0e+00, up in 33 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.702× (z -5.1, q 2e-04, down in 16 of 41 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSPN]] (+0.67, fdr 1e-05), [[HFE]] (+0.64, fdr 9e-05), [[HOXB-AS1]] (+0.63, fdr 1e-04); moves opposite to [[GIPC1]] (-0.63, fdr 5e-05), [[ANKRD27]] (-0.56, fdr 7e-04), [[SNRPD2]] (-0.55, fdr 4e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4103.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.61×** | +25.3 | 0e+00 | 33/35 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.07×** | +10.7 | 3e-24 | 20/34 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.56×** | +9.4 | 9e-19 | 4/7 (CFPAC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.41×** | +9.1 | 9e-18 | 8/15 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +7.0 | 4e-10 | 16/30 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +6.9 | 6e-10 | 8/18 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.95×** | +6.7 | 2e-09 | 19/38 (LoVo, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +6.5 | 4e-09 | 4/9 (BT-474, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.82×** | +6.2 | 3e-08 | 17/43 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +6.2 | 4e-08 | 17/36 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +5.1 | 1e-05 | 10/42 (RKO, NCI-H2030, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.002 | 10/42 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +4.0 | 0.003 | 7/40 (LOX-IMVI, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.024 | 9/33 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4103.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.702×** | -5.1 | 2e-04 | 16/41 (hTERT-HPNE, HEC-1-A, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.616×** | -5.0 | 2e-04 | 17/43 (A-172, HOP62, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.617×** | -4.8 | 3e-04 | 13/41 (A549, RPMI-7951, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.682×** | -3.9 | 0.008 | 10/42 (hTERT-HPNE, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.685×** | -3.9 | 0.008 | 11/41 (RPMI-7951, hTERT-HPNE, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.686×** | -3.9 | 0.008 | 14/37 (hTERT-HPNE, SW 900, …) | rises with dose |  |
| [[vincristine (drug)]] 0.05 µM |  | **0.671×** | -3.9 | 0.008 | 10/42 (NCI-H23, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | **0.699×** | -3.7 | 0.016 | 6/43 (C-33 A, A-427, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.710×** | -3.5 | 0.028 | 13/42 (hTERT-HPNE, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.728×** | -3.3 | 0.058 | 8/34 (SW480, HOP62, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.728×** | -3.3 | 0.058 | 14/42 (hTERT-HPNE, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.732×** | -3.2 | 0.065 | 7/41 (hTERT-HPNE, SW 900, …) | rises with dose | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.559×** | -3.1 | 0.075 | 5/36 (MIA PaCa-2, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.739×** | -3.1 | 0.076 | 9/43 (MIA PaCa-2, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.741×** | -3.1 | 0.076 | 11/37 (hTERT-HPNE, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.742×** | -3.1 | 0.076 | 14/42 (LOX-IMVI, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Adagrasib (drug)]] 5 µM |  | **0.741×** | -3.0 | 0.097 | 8/43 (SW 900, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4103. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 2.10 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 4.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.65× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 2.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.57× (z +9.2) | — |
| [[LoVo (line)]] | wt | 2.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.70× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 2.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.45× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 2.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.3× (z +13.8) | — |
| [[Panc 03.27 (line)]] | alt | 2.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 1.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.33× (z +10.2) | — |
| [[SW480 (line)]] | alt | 1.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +11.4) | — |
| [[A-172 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.617 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.975 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.898 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.873 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.568 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4103), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSPN]] | +0.67 | +0.49 / +0.51 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[HFE]] | +0.64 | +0.37 / +0.53 | both halves | 9e-05 |  |
| [[HOXB-AS1]] | +0.63 | +0.51 / +0.34 | both halves | 1e-04 |  |
| [[STARD4-AS1]] | +0.63 | +0.54 / +0.35 | both halves | 1e-04 |  |
| [[ZC2HC1C]] | +0.63 | +0.58 / +0.36 | both halves | 1e-04 |  |
| [[EFCAB5]] | +0.62 | +0.58 / +0.21 | both halves | 6e-04 |  |
| [[INPPL1]] | +0.62 | +0.36 / +0.43 | both halves | 9e-05 |  |
| [[USP11]] | +0.61 | +0.58 / +0.38 | both halves | 7e-05 |  |
| [[ZNF827]] | +0.61 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[LINC03048]] | +0.61 | +0.56 / +0.32 | both halves | 1e-04 |  |
| [[PHYH]] | +0.61 | +0.59 / +0.38 | both halves | 7e-05 |  |
| [[PBLD]] | +0.60 | +0.48 / +0.18 | ⚠ not reproduced | 1e-03 |  |
| [[PRRT2]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GIPC1]] | -0.63 | -0.40 / -0.44 | both halves | 5e-05 | pathway: Signaling by TGFB family members |
| [[ANKRD27]] | -0.56 | -0.48 / -0.20 | both halves | 7e-04 |  |
| [[SNRPD2]] | -0.55 | -0.45 / -0.26 | both halves | 4e-04 |  |
| [[RRP1B]] | -0.55 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[TMEM120B]] | -0.55 | -0.52 / -0.21 | both halves | 6e-04 |  |
| [[RPS5]] | -0.55 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[RALGAPA2]] | -0.54 | -0.38 / -0.24 | both halves | 4e-04 |  |
| [[CLTCL1]] | -0.54 | -0.31 / -0.25 | both halves | 4e-04 |  |
| [[PCMT1]] | -0.54 | -0.47 / -0.10 | ⚠ not reproduced | 0.003 |  |
| [[ANKS6]] | -0.53 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[RMND1]] | -0.53 | -0.29 / -0.28 | both halves | 3e-04 |  |
| [[NAA10]] ⚠ | -0.53 | -0.25 / -0.21 | both halves | 7e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[COMMD2]] | -0.53 | -0.36 / -0.21 | both halves | 6e-04 |  |
| [[NUDCD3]] | -0.52 | -0.50 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TGFB3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HOXB2]] | B | HOXB2 activity raises TGFB3's level | lines that do not express HOXB2 (21) vs lines expressing it (29) | 1.36× lower at baseline in the lines without HOXB2 | 0.073 | ⚠ within organs, on part of the lines; also absent: HOXB-AS1, SOX2, JAKMIP2-AS1 |
| [[PDZRN3]] | B | PDZRN3 activity raises TGFB3's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 1.40× lower at baseline in the lines without PDZRN3 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.602). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (5.2, 25.5); signed map (36.0, -3.6). **Vector** length 61.7, 8.78% of its response variance represented; |z| ≥ 3 in 1,127 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.4 | +25.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +9.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +10.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.0 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.0 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.0 | +1.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.3 | -3.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.2 | -3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -5.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.0 | -1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.6 | -3.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | transforming growth factor beta 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:75,958,097-75,983,011 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ARVD1, ARVD |
| Gene groups (HGNC) | Transforming growth factor beta family |
| Hallmark sets | HYPOXIA |
| Reactome | 11 pathways, smallest: Molecules associated with elastic fibres; Elastic fibre formation; TGF-beta receptor signaling activates SMADs |
| Matched by | ensembl_id |

**Function**, from UniProt [P10600](https://www.uniprot.org/uniprotkb/P10600) (Transforming growth factor beta-3 proprotein):

> Transforming growth factor beta-3 proprotein: Precursor of the Latency-associated peptide (LAP) and Transforming growth factor beta-3 (TGF-beta-3) chains, which constitute the regulatory and active subunit of TGF-beta-3, respectively.; [Latency-associated peptide]: Required to maintain the Transforming growth factor beta-3 (TGF-beta-3) chain in a latent state during storage in extracellular matrix (By similarity). Associates non-covalently with TGF-beta-3 and regulates its activation via …

**Summary**, from NCBI Gene [7043](https://www.ncbi.nlm.nih.gov/gene/7043):

> This gene encodes a secreted ligand of the TGF-beta (transforming growth factor-beta) superfamily of proteins. Ligands of this family bind various TGF-beta receptors leading to recruitment and activation of SMAD family transcription factors that regulate gene expression. The encoded preproprotein is proteolytically processed to generate a latency-associated peptide (LAP) and a mature peptide, and is found in either a latent form composed of a mature peptide homodimer, a LAP homodimer, and a …

**Accessions** — [HGNC:11769](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11769) · Entrez [7043](https://www.ncbi.nlm.nih.gov/gene/7043) · UniProt [P10600](https://www.uniprot.org/uniprotkb/P10600) · Ensembl [ENSG00000119699](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119699)

## Data

Gene col 4103: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4103); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4103, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4103]; `tensor/DDL_lfc|DDL_z.npy` [4103]; `embed/gene_vectors.npy` [4103]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4103 or target_col == 4103). Every well: [[TGFB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TGFB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
