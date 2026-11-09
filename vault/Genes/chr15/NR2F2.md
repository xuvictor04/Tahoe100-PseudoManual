---
symbol: "NR2F2"
type: "gene"
col: 11695
ensembl_id: "ENSG00000185551"
name: "nuclear receptor subfamily 2 group F member 2"
location: "15q26.2"
module: 144
arm: "+"
pooled_cpm: 53.28
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 17
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# NR2F2

*nuclear receptor subfamily 2 group F member 2* — 15q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.58× (z +7.6, q 2e-11, up in 26 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (A549 4.68×, NCI-H460 2.52×, RKO 3.67×, SW480 2.20×); [[Homoharringtonine (drug)]] 5 µM in 3 lines (LS 180 2.85×, KATO III 2.56×, SW1417 2.50×; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (MIA PaCa-2 14.7×; ⚠ cell-cycle shift, explains ~31% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (HOP62 13.1×).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.495× (z -8.2, q 1e-13, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PURA]] (+0.65, fdr 7e-06), [[NOG]] (+0.63, fdr 3e-05), [[HCFC1R1]] (+0.59, fdr 1e-05); moves opposite to [[JMJD7]] (-0.59, fdr 1e-05), [[DELE1]] (-0.53, fdr 3e-05), [[CYP2D7]] (-0.51, fdr 3e-05).
> It is in [[Module 144]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NR2F2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11695.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (A549 4.68×, NCI-H460 2.52×, RKO 3.67×, SW480 2.20×); [[Homoharringtonine (drug)]] 5 µM in 3 lines (LS 180 2.85×, KATO III 2.56×, SW1417 2.50×; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (MIA PaCa-2 14.7×; ⚠ cell-cycle shift, explains ~31% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (HOP62 13.1×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +7.6 | 2e-11 | 26/47 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.81×** | +3.6 | 0.083 | 21/48 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | 1.68× | +3.2 | 0.19 | 15/46 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | 1.31× | +3.2 | 0.19 | 22/46 (LS 180, HT-29, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.31× | +3.1 | 0.19 | 20/46 (LS 180, SW480, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.21× | +3.1 | 0.19 | 20/47 (HOP62, NCI-H2030, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 1.20× | +3.0 | 0.19 | 19/47 (MIA PaCa-2, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11695.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.495×** | -8.2 | 1e-13 | 39/47 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.510×** | -7.9 | 1e-12 | 39/46 (HOP62, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.538×** | -7.2 | 9e-11 | 36/47 (Panc 03.27, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.551×** | -6.5 | 1e-08 | 35/47 (HOP62, J82, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.595×** | -6.0 | 2e-07 | 33/47 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.724×** | -5.3 | 1e-05 | 31/47 (NCI-H2347, Panc 03.27, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.644×** | -5.1 | 2e-05 | 29/47 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.680×** | -4.5 | 5e-04 | 36/47 (HOP62, NCI-H2347, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.702×** | -4.1 | 0.002 | 25/47 (NCI-H2347, HOP62, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.720×** | -3.8 | 0.007 | 24/46 (HCT15, KATO III, …) | top dose only | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.720×** | -3.8 | 0.007 | 25/46 (KATO III, NCI-H1792, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.728×** | -3.7 | 0.011 | 22/47 (NCI-H2347, J82, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.741×** | -3.5 | 0.021 | 27/47 (HOP62, NCI-H2347, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.571×** | -3.4 | 0.026 | 19/47 (J82, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[DTP3 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.757×** | -3.2 | 0.045 | 21/47 (NCI-H1792, A-172, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.763×** | -3.2 | 0.057 | 21/47 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.771×** | -3.0 | 0.082 | 18/47 (HOP62, J82, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.68 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11695. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 137 | 1 | 22 (7 ⚠) | [[PH-797804 (drug)]] 5 µM 13.1× (z +9.7) | [[Ixazomib citrate (drug)]] 5 µM 0.136× (z -14.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.145× (z -13.9) |
| [[NCI-H2347 (line)]] | alt | 82.1 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.244× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 159 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -11.8) |
| [[J82 (line)]] | alt | 81.3 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.354× (z -11.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.310× (z -9.2) |
| [[A-427 (line)]] | wt | 67.1 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.332× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 122 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -12.4) |
| [[CFPAC-1 (line)]] | alt | 137 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.281× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 87.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.339× (z -9.0) |
| [[SNU-423 (line)]] | alt | 92.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.255× (z -9.4) |
| [[AN3 CA (line)]] | alt | 81.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.125× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.172× (z -9.0) |
| [[HT-29 (line)]] | alt | 54.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.287× (z -9.8) |
| [[KATO III (line)]] | alt | 49.0 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.356× (z -8.7) |
| [[LoVo (line)]] | wt | 92.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 34.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 22.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.68× (z +12.9) | — |
| [[C-33 A (line)]] | alt | 51.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.187× (z -9.5) |
| [[HCT15 (line)]] | alt | 107 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.181× (z -11.4) |
| [[HepG2_C3A (line)]] | wt | 13.8 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.112× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 69.9 | 1 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 14.7× (z +10.4) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1792 (line)]] | alt | 62.9 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.259× (z -8.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H460 (line)]] | wt | 21.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +9.3) | — |
| [[NCI-H661 (line)]] | alt | 124 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.126× (z -9.9) |
| [[RKO (line)]] | wt | 16.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 41.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW480 (line)]] | alt | 28.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +9.1) | — |
| [[A-172 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 90.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 61.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11695), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PURA]] | +0.65 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[NOG]] | +0.63 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[HCFC1R1]] | +0.59 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[IMP3]] | +0.59 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[NR2F2-AS1]] | +0.58 | +0.53 / +0.61 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[YY1]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 | STRING 528 |
| [[KDM2B]] | +0.55 | +0.41 / +0.65 | both halves | 4e-05 | same gene group |
| [[RSBN1]] | +0.54 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[FOXD1]] | +0.54 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[IPMK]] | +0.53 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[ZIC2]] | +0.52 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[TRIM7-AS2]] | +0.52 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[TGIF2]] | +0.52 | +0.49 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JMJD7]] | -0.59 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[DELE1]] | -0.53 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[CYP2D7]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[ENTPD6]] | -0.50 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[ADAMTSL5]] | -0.49 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[PYGB]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[HSD17B4]] | -0.48 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[PRELID3B]] | -0.47 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[PTPN11]] | -0.47 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[GSR]] | -0.46 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[RNF32-AS1]] | -0.45 | -0.40 / -0.46 | both halves | 4e-05 |  |
| [[OCRL]] | -0.45 | -0.36 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR2F2-AS1]] | B | NR2F2-AS1 activity raises NR2F2's level | lines that do not express NR2F2-AS1 (8) vs lines expressing it (42) | 2.09× lower at baseline in the lines without NR2F2-AS1 | 0.062 | ⚠ within organs, on part of the lines; also absent: TMEFF1, RIMKLB, LHFPL6 |
| [[FAT4]] | B | FAT4 activity raises NR2F2's level | lines that do not express FAT4 (20) vs lines expressing it (30) | 1.61× lower at baseline in the lines without FAT4 | 0.065 | ⚠ within organs, on part of the lines; also absent: RFTN1, GPR176, GNG11 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.592). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.1, -19.4); signed map (-32.3, 31.2). **Vector** length 121, 34.8% of its response variance represented; |z| ≥ 3 in 1,135 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +5.3 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.5 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +1.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +3.3 | +3.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +2.0 | +2.0 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -10.5 | -0.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -9.5 | -0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -9.4 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -7.0 | -7.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | -6.4 | -6.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.0 | -6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -5.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.6 | -4.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.6 | -3.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.4 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor subfamily 2 group F member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.2 — chr15:96,325,938-96,340,263 (+) |
| Ensembl biotype | protein_coding |
| Also known as | COUP-TFII, COUPTFB, SVP40, NF-E3, COUPTF2; previously ARP1, TFCOUP2 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Nuclear receptor subfamily 2 group F |
| Reactome | 8 pathways, smallest: Interaction of NuRD complexes with transcription factors; NuRD complex assembly; CHD3, CHD4, CHD5 subfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [P24468](https://www.uniprot.org/uniprotkb/P24468) (COUP transcription factor 2):

> Ligand-activated transcription factor. Activated by high concentrations of 9-cis-retinoic acid and all-trans-retinoic acid, but not by dexamethasone, cortisol or progesterone (in vitro). Regulation of the apolipoprotein A-I gene transcription. Binds to DNA site A. May be required to establish ovary identity during early gonad development.

**Summary**, from NCBI Gene [7026](https://www.ncbi.nlm.nih.gov/gene/7026):

> This gene encodes a member of the steroid thyroid hormone superfamily of nuclear receptors. The encoded protein is a ligand inducible transcription factor that is involved in the regulation of many different genes. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:7976](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7976) · Entrez [7026](https://www.ncbi.nlm.nih.gov/gene/7026) · UniProt [P24468](https://www.uniprot.org/uniprotkb/P24468) · Ensembl [ENSG00000185551](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185551)

## Data

Gene col 11695: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11695); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11695, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11695]; `tensor/DDL_lfc|DDL_z.npy` [11695]; `embed/gene_vectors.npy` [11695]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11695 or target_col == 11695). Every well: [[NR2F2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NR2F2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
