---
symbol: "PLS3-AS1"
type: "gene"
col: 15696
ensembl_id: "ENSG00000271826"
name: "PLS3 antisense RNA 1"
location: "Xq23"
module: 199
arm: "+"
pooled_cpm: 6.03
n_lines_expressing: 40
n_dd_up: 31
n_dd_down: 4
n_dd_up_clean: 28
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 12
tags: ["gene", "module/199"]
generated_by: "tahoemap"
---

# PLS3-AS1

*PLS3 antisense RNA 1* — Xq23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.30× (z +21.1, q 0e+00, up in 28 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.524× (z -5.6, q 1e-05, down in 18 of 28 measured lines) ⚠ toxic. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 0.666× (z -3.7, q 0.049, down in 13 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.158×; ⚠ cell-cycle shift, explains ~35% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (Hs 766T 0.0901×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (PANC-1 0.176×; ⚠ toxic); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H23 0.194×); [[Ponatinib (drug)]] 5 µM in 1 line (C32 0.161×).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCNX4-DT]] (+0.77, fdr 1e-05), [[ANKRD18B]] (+0.73, fdr 3e-05), [[TMEM202-AS1]] (+0.72, fdr 1e-04); moves opposite to [[PCMT1]] (-0.63, fdr 0.001, ⚠ one half only (not replicated)), [[KIF21B]] (-0.63, fdr 1e-04), [[NAPG]] (-0.62, fdr 1e-04), [[APMAP]] (-0.61, fdr 4e-05).
> It is in [[Module 199]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SYT9-AS1]] → it (grade B ⚠); 12 go from it, the strongest it → [[DPY19L2P2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15696.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.30×** | +21.1 | 0e+00 | 28/31 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.34×** | +15.2 | 0e+00 | 29/31 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.59×** | +11.0 | 8e-26 | 26/30 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.99×** | +9.4 | 6e-19 | 23/33 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.47×** | +8.1 | 7e-14 | 16/29 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.75×** | +7.1 | 1e-10 | 15/37 (NCI-H460, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.05×** | +6.4 | 1e-08 | 25/37 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.65×** | +6.4 | 2e-08 | 20/37 (NCI-H460, AN3 CA, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.82×** | +5.1 | 2e-05 | 17/34 (KATO III, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +5.0 | 4e-05 | 9/24 (A498, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.67×** | +4.5 | 4e-04 | 13/34 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.67×** | +4.4 | 4e-04 | 17/37 (SW480, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.63×** | +4.4 | 6e-04 | 15/36 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.61×** | +4.2 | 9e-04 | 12/37 (NCI-H2030, NCI-H1573, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.52×** | +4.2 | 9e-04 | 14/34 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.59×** | +4.1 | 0.001 | 12/33 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15696.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.158×; ⚠ cell-cycle shift, explains ~35% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (Hs 766T 0.0901×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (PANC-1 0.176×; ⚠ toxic); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H23 0.194×); [[Ponatinib (drug)]] 5 µM in 1 line (C32 0.161×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.524×** | -5.6 | 1e-05 | 18/28 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.628×** | -4.1 | 0.011 | 15/36 (NCI-H23, CHP-212, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.666×** | -3.7 | 0.049 | 13/35 (H4, SW1417, …) | two highest doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.659×** | -3.4 | 0.083 | 10/37 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | 0.485× | -3.2 | 0.13 | 8/29 (SW480, NCI-H23, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.700× | -3.2 | 0.13 | 10/37 (PANC-1, SW480, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.704× | -3.2 | 0.13 | 14/37 (NCI-H23, NCI-H1573, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15696. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.75 | 3 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +9.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -11.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[KATO III (line)]] | alt | 12.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +18.3) | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 26.2 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +12.6) | [[Belumosudil (drug)]] 5 µM 0.194× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 6.03 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.9× (z +18.2) | — |
| [[Hs 766T (line)]] | wt | 10.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +15.6) | [[Docetaxel (drug)]] 0.05 µM 0.0901× (z -10.7) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 6.53 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +13.5) | — |
| [[A-172 (line)]] | wt | 4.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +12.3) | — |
| [[C32 (line)]] | wt | 16.8 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.161× (z -8.5) |
| [[HCT15 (line)]] | alt | 4.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 17.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +8.8) | — |
| [[J82 (line)]] | alt | 5.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +14.2) | — |
| [[LOX-IMVI (line)]] | wt | 6.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 10.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.71× (z +11.8) | — |
| [[RPMI-7951 (line)]] | alt | 6.11 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.74× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 7.46 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +13.1) | — |
| [[SNU-423 (line)]] | alt | 8.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.36× (z +8.8) | — |
| [[A-427 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.663 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.732 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.774 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.712 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.809 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15696), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 16 of them with an alert (⚠; 16 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCNX4-DT]] | +0.77 | +0.78 / +0.50 | both halves | 1e-05 |  |
| [[ANKRD18B]] | +0.73 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[TMEM202-AS1]] | +0.72 | +0.73 / +0.35 | both halves | 1e-04 | same gene group |
| [[GALNT7-DT]] | +0.72 | +0.74 / +0.27 | both halves | 3e-04 |  |
| [[CCDC90B-AS1]] | +0.71 | +0.77 / +0.19 | ⚠ one half (not replicated) | 8e-04 | same gene group |
| [[DPH6-DT]] | +0.71 | +0.74 / +0.43 | both halves | 3e-05 |  |
| [[NQO1-DT]] | +0.69 | +0.76 / +0.27 | both halves | 3e-04 |  |
| [[AHI1-DT]] | +0.69 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[PATL2]] | +0.69 | +0.74 / +0.25 | both halves | 4e-04 |  |
| [[OXA1L-DT]] | +0.69 | +0.68 / +0.34 | both halves | 1e-04 |  |
| [[MZF1-AS1]] | +0.69 | +0.73 / +0.24 | both halves | 5e-04 | same gene group |
| [[TCEAL4]] | +0.68 | +0.66 / +0.36 | both halves | 1e-04 |  |
| [[PPP1R12A-AS2]] | +0.68 | +0.70 / +0.25 | both halves | 4e-04 | same gene group |

## Genes that move opposite

*7 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCMT1]] | -0.63 | -0.60 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[KIF21B]] | -0.63 | -0.59 / -0.33 | both halves | 1e-04 |  |
| [[NAPG]] | -0.62 | -0.62 / -0.33 | both halves | 1e-04 |  |
| [[APMAP]] | -0.61 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[GPRIN1]] | -0.61 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[GTPBP3]] | -0.60 | -0.52 / -0.22 | both halves | 6e-04 |  |
| [[ST6GALNAC4]] | -0.60 | -0.60 / -0.12 | ⚠ one half (not replicated) | 0.002 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYT9-AS1]] | B | SYT9-AS1 activity raises PLS3-AS1's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 2.14× lower at baseline in the lines without SYT9-AS1 | 0.006 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ANKRD20A21P]] | B | ANKRD20A21P activity raises PLS3-AS1's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 1.65× lower at baseline in the lines without ANKRD20A21P | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[TOP2A]] | B | TOP2A activity lowers PLS3-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MYPN]] | B | MYPN activity raises PLS3-AS1's level | lines that do not express MYPN (29) vs lines expressing it (21) | 1.52× lower at baseline in the lines without MYPN | 0.084 | ⚠ within organs, on part of the lines; also absent: COL4A6, EPGN, FLRT2 |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPY19L2P2]] | B | PLS3-AS1 activity raises DPY19L2P2's level | lines that do not express PLS3-AS1 (10) vs lines expressing it (40) | 1.88× lower at baseline in the lines without PLS3-AS1 | 0.026 | ⚠ within organs, on part of the lines; also absent: COPZ2, CAV2, DNAI1 |
| [[PAXIP1-AS2]] | B | PLS3-AS1 activity raises PAXIP1-AS2's level | lines that do not express PLS3-AS1 (10) vs lines expressing it (40) | 1.67× lower at baseline in the lines without PLS3-AS1 | 0.039 | ⚠ within organs, on part of the lines; also absent: COPZ2, CAV2, DNAI1 |
| [[DPY19L2]] | B | PLS3-AS1 activity raises DPY19L2's level | lines that do not express PLS3-AS1 (10) vs lines expressing it (40) | 2.51× lower at baseline in the lines without PLS3-AS1 | 0.048 | ⚠ within organs, on part of the lines; also absent: COPZ2, CAV2, DNAI1 |
| [[FLRT2]] | B | PLS3-AS1 activity raises FLRT2's level | lines that do not express PLS3-AS1 (10) vs lines expressing it (40) | 3.70× lower at baseline in the lines without PLS3-AS1 | 0.068 | ⚠ within organs, on part of the lines; also absent: COPZ2, CAV2, DNAI1 |
| [[PIGP]] | B | PLS3-AS1 activity raises PIGP's level | lines that do not express PLS3-AS1 (10) vs lines expressing it (40) | 1.15× lower at baseline in the lines without PLS3-AS1 | 0.074 | ⚠ within organs, on part of the lines; also absent: COPZ2, CAV2, DNAI1 |
| [[MAILR]] | B | PLS3-AS1 activity raises MAILR's level | lines that do not express PLS3-AS1 (10) vs lines expressing it (40) | 1.50× lower at baseline in the lines without PLS3-AS1 | 0.077 | ⚠ within organs, on part of the lines; also absent: COPZ2, CAV2, DNAI1 |
| [[UNC13B]] | B | PLS3-AS1 activity lowers UNC13B's level | lines that do not express PLS3-AS1 (10) vs lines expressing it (40) | 2.00× higher at baseline in the lines without PLS3-AS1 | 0.078 | ⚠ within organs, on part of the lines; also absent: COPZ2, CAV2, DNAI1 |
| [[PBLD]] | B | PLS3-AS1 activity raises PBLD's level | lines that do not express PLS3-AS1 (10) vs lines expressing it (40) | 1.27× lower at baseline in the lines without PLS3-AS1 | 0.083 | ⚠ within organs, on part of the lines; also absent: COPZ2, CAV2, DNAI1 |
| [[ZCCHC8]] | B | PLS3-AS1 activity lowers ZCCHC8's level | lines that do not express PLS3-AS1 (10) vs lines expressing it (40) | 1.32× higher at baseline in the lines without PLS3-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: COPZ2, CAV2, DNAI1 |
| [[TGM2]] | B | PLS3-AS1 activity raises TGM2's level | lines that do not express PLS3-AS1 (10) vs lines expressing it (40) | 3.13× lower at baseline in the lines without PLS3-AS1 | 0.091 | ⚠ within organs, on part of the lines; also absent: COPZ2, CAV2, DNAI1 |
| [[LRRC37A3]] | B | PLS3-AS1 activity raises LRRC37A3's level | lines that do not express PLS3-AS1 (10) vs lines expressing it (40) | 1.27× lower at baseline in the lines without PLS3-AS1 | 0.095 | ⚠ within organs, on part of the lines; also absent: COPZ2, CAV2, DNAI1 |
| [[NUTM2E]] | B | PLS3-AS1 activity raises NUTM2E's level | lines that do not express PLS3-AS1 (10) vs lines expressing it (40) | 1.17× lower at baseline in the lines without PLS3-AS1 | 0.096 | ⚠ within organs, on part of the lines; also absent: COPZ2, CAV2, DNAI1 |

## Where it sits

- **Module**: [[Module 199]]; 16 genes; every member is in the + arm (projection on the module's main direction -0.748). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.4, 12.8); signed map (25.5, -11.9). **Vector** length 79.4, 17.7% of its response variance represented; |z| ≥ 3 in 875 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.0 | +21.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +15.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +6.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.6 | +7.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +6.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +2.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.3 | +4.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -6.1 | -4.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -5.9 | -3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | -2.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -3.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +1.5 |

## What is on record

|  |  |
|---|---|
| Name | PLS3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | Xq23 — chrX:115,518,182-115,562,731 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50343](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50343) · Entrez [101927352](https://www.ncbi.nlm.nih.gov/gene/101927352) · Ensembl [ENSG00000271826](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000271826)

## Data

Gene col 15696: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15696); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15696, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15696]; `tensor/DDL_lfc|DDL_z.npy` [15696]; `embed/gene_vectors.npy` [15696]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15696 or target_col == 15696). Every well: [[PLS3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLS3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
