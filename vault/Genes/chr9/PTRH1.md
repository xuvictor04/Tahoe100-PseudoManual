---
symbol: "PTRH1"
type: "gene"
col: 11878
ensembl_id: "ENSG00000187024"
name: "peptidyl-tRNA hydrolase 1 homolog"
location: "9q34.11"
module: 45
arm: "-"
pooled_cpm: 6.84
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# PTRH1

*peptidyl-tRNA hydrolase 1 homolog* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (16 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.87× (z +29.3, q 0e+00, up in 41 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 0.544× (z -4.9, q 6e-04, down in 12 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (NCI-H23 0.0712×; ⚠ transcription drop); [[TAK-901 (drug)]] 0.05 µM in 1 line (LOX-IMVI 0.0533×); [[Berberine (chloride hydrate) (drug)]] 0.5 µM in 1 line (C32 0.0486×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.113×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXW9]] (+0.57, fdr 3e-05), [[LYRM4]] (+0.57, fdr 1e-05), [[ZNF710]] (+0.56, fdr 1e-04); moves opposite to [[HLTF]] (-0.55, fdr 1e-05), [[RHOXF1]] (-0.54, fdr 1e-05), [[SNX2]] (-0.54, fdr 1e-05).
> It sits in the **-** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 16 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11878.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.87×** | +29.3 | 0e+00 | 41/41 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.47×** | +13.8 | 4e-41 | 40/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.39×** | +13.3 | 5e-38 | 37/47 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.19×** | +12.0 | 7e-31 | 38/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.12×** | +10.6 | 3e-24 | 14/20 (A498, SNU-423, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.97×** | +10.0 | 2e-21 | 5/11 (CFPAC-1, NCI-H2030, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.91×** | +9.5 | 2e-19 | 22/40 (NCI-H460, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +9.5 | 2e-19 | 26/48 (BT-474, HEC-1-A, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.81×** | +9.1 | 8e-18 | 28/42 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +6.5 | 4e-09 | 19/42 (A-172, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +6.5 | 4e-09 | 19/47 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.55×** | +6.4 | 7e-09 | 20/31 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **1.49×** | +6.1 | 4e-08 | 15/29 (HT-29, LS 180, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.49×** | +5.8 | 2e-07 | 20/43 (NCI-H460, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +5.3 | 5e-06 | 10/34 (NCI-H2347, AsPC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +4.8 | 4e-05 | 9/45 (A-427, HS-578T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +4.5 | 2e-04 | 11/43 (NCI-H460, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.32×** | +3.9 | 0.003 | 8/38 (SHP-77, SW480, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.004 | 8/44 (SK-MEL-2, PANC-1, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.004 | 7/45 (PANC-1, COLO 205, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.59×** | +3.7 | 0.005 | 2/44 (KATO III, NCI-H460) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.18× | +3.5 | 0.011 | 6/47 (BT-474, SHP-77, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.024 | 9/46 (MIA PaCa-2, A498, …) | two highest doses |  |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.26×** | +3.2 | 0.027 | 5/39 (J82, KATO III, …) | inconsistent across doses |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.049 | 6/40 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11878.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (NCI-H23 0.0712×; ⚠ transcription drop); [[TAK-901 (drug)]] 0.05 µM in 1 line (LOX-IMVI 0.0533×); [[Berberine (chloride hydrate) (drug)]] 0.5 µM in 1 line (C32 0.0486×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.113×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.544×** | -4.9 | 6e-04 | 12/36 (LOX-IMVI, A-427, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.815× | -3.2 | 0.30 | 9/44 (A498, AsPC-1, …) | all doses, flat |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.818× | -3.1 | 0.30 | 7/47 (SK-MEL-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.820× | -3.1 | 0.30 | 5/46 (NCI-H2030, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11878. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 10.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +10.1) | — |
| [[NCI-H460 (line)]] | wt | 6.61 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.55× (z +14.2) | — |
| [[RKO (line)]] | wt | 17.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +9.7) | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.219× (z -8.5) |
| [[A498 (line)]] | wt | 10.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +11.6) | — |
| [[A549 (line)]] | wt | 7.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.45× (z +10.9) | — |
| [[AsPC-1 (line)]] | alt | 5.54 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0880× (z -9.0) |
| [[BT-474 (line)]] | alt | 16.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +10.5) | — |
| [[C32 (line)]] | wt | 6.16 | 0 | 1 | — | [[Berberine (chloride hydrate) (drug)]] 0.5 µM 0.0486× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 6.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.27× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 7.14 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0950× (z -9.4) |
| [[J82 (line)]] | alt | 11.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +11.4) | — |
| [[LoVo (line)]] | wt | 4.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 5.91 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0533× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 3.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 6.14 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.113× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 8.72 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0712× (z -12.6) ⚠ transcription drop |
| [[PANC-1 (line)]] | alt | 6.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 4.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.90× (z +8.7) | — |
| [[SW480 (line)]] | alt | 6.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +10.7) | — |
| [[A-427 (line)]] | wt | 8.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11878), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW9]] | +0.57 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[LYRM4]] | +0.57 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[ZNF710]] | +0.56 | +0.33 / +0.61 | both halves | 1e-04 |  |
| [[AXIN1]] | +0.55 | +0.26 / +0.67 | both halves | 4e-04 |  |
| [[MAD1L1]] | +0.54 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[UBE2F-SCLY]] | +0.52 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[CENPT]] | +0.52 | +0.26 / +0.58 | both halves | 4e-04 |  |
| [[GATAD2A]] | +0.52 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[RELL2]] | +0.52 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[MROH1]] | +0.52 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[PYCR3]] | +0.52 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[TMEM11-DT]] | +0.51 | +0.34 / +0.54 | both halves | 1e-04 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HLTF]] | -0.55 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[RHOXF1]] | -0.54 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[SNX2]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[TNRC6A]] | -0.53 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[NDUFA5]] | -0.53 | -0.37 / -0.61 | both halves | 8e-05 |  |
| [[MRPS31P4]] | -0.53 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[LINC00888]] | -0.52 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[GTPBP8]] | -0.52 | -0.29 / -0.52 | both halves | 3e-04 |  |
| [[NUDT12]] | -0.51 | -0.30 / -0.54 | both halves | 2e-04 |  |
| [[UBXN2B]] | -0.51 | -0.43 / -0.54 | both halves | 4e-05 |  |
| [[ALDH7A1]] | -0.51 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[BPNT1]] | -0.51 | -0.42 / -0.58 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PTRH1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **-** arm (projection on the module's main direction -0.490). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-16.0, 2.7); signed map (-22.0, 1.4). **Vector** length 59.9, 8.47% of its response variance represented; |z| ≥ 3 in 985 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +29.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +2.8 | +10.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.7 | +9.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +2.5 | +5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.7 | +3.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.7 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -2.3 |
|  | [[NG25 (drug)]] 5 µM |  | -2.6 | -4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.2 | -3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | +0.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | peptidyl-tRNA hydrolase 1 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:127,690,348-127,724,873 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PTH1; previously C9orf115 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86Y79](https://www.uniprot.org/uniprotkb/Q86Y79) (Peptidyl-tRNA hydrolase):

> Peptidyl-tRNA hydrolase that cleaves nascent chains-tRNAs that are not stably fixed in the P-site of 60S ribosome-nascent chain complexes. Acts downstream of the ribosome-associated quality control (RQC) pathway to release non-ubiquitinated nascent chains from 60S and 80S ribosome-nascent chain complexes. Does not act on ubiquitinated nascent chains, which are cleaved by ANKZF1 for degradation.

**Summary**, from NCBI Gene [138428](https://www.ncbi.nlm.nih.gov/gene/138428):

> Enables peptidyl-tRNA hydrolase activity. Involved in rescue of stalled cytosolic ribosome. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27039](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27039) · Entrez [138428](https://www.ncbi.nlm.nih.gov/gene/138428) · UniProt [Q86Y79](https://www.uniprot.org/uniprotkb/Q86Y79) · Ensembl [ENSG00000187024](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187024)

## Data

Gene col 11878: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11878); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11878, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11878]; `tensor/DDL_lfc|DDL_z.npy` [11878]; `embed/gene_vectors.npy` [11878]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11878 or target_col == 11878). Every well: [[PTRH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTRH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
