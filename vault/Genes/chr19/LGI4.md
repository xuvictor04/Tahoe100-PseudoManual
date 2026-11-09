---
symbol: "LGI4"
type: "gene"
col: 7747
ensembl_id: "ENSG00000153902"
name: "leucine rich repeat LGI family member 4"
location: "19q13.12"
module: 100
arm: "+"
pooled_cpm: 2.39
n_lines_expressing: 45
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 12
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# LGI4

*leucine rich repeat LGI family member 4* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.21× (z +13.9, q 2e-41, up in 17 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.575× (z -4.7, q 0.002, down in 13 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1573 0.147×, NCI-H23 0.234×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H23 0.0685×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KANK3]] (+0.60, fdr 1e-05), [[CDH23]] (+0.57, fdr 8e-05), [[HES2]] (+0.56, fdr 8e-05); moves opposite to [[ATP5PB]] (-0.60, fdr 1e-05), [[C2CD5]] (-0.53, fdr 5e-05), [[SLX4IP]] (-0.51, fdr 6e-05).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 12 go from it, the strongest it → cells under [[Ouabain (Octahydrate) (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7747.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.21×** | +13.9 | 2e-41 | 17/25 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.40×** | +10.4 | 1e-22 | 2/6 (NCI-H2030, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.41×** | +10.0 | 4e-21 | 1/2 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.03×** | +9.4 | 1e-18 | 22/39 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.55×** | +7.9 | 3e-13 | 23/36 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.55×** | +7.6 | 3e-12 | 9/19 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.34×** | +7.2 | 5e-11 | 11/26 (NCI-H23, HCT15, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.81×** | +7.1 | 1e-10 | 13/39 (A498, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +5.9 | 2e-07 | 6/9 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.93×** | +5.1 | 2e-05 | 1/3 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.84×** | +4.8 | 9e-05 | 6/15 (NCI-H1573, A498, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.74×** | +4.7 | 1e-04 | 9/39 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +4.1 | 0.002 | 11/32 (NCI-H460, LoVo, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.003 | 11/38 (KATO III, SW480, …) | rises with dose | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.82×** | +3.6 | 0.011 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.53×** | +3.6 | 0.011 | 9/36 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +3.5 | 0.013 | 7/28 (NCI-H460, H4, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +3.3 | 0.027 | 6/32 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +3.3 | 0.033 | 7/35 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.059 | 4/37 (A498, SW480, …) | top dose only |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.070 | 2/28 (PANC-1, Hs 766T) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7747.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1573 0.147×, NCI-H23 0.234×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H23 0.0685×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.575×** | -4.7 | 0.002 | 13/25 (NCI-H23, HT-29, …) | two highest doses | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.652× | -3.5 | 0.14 | 13/33 (NCI-H1573, SW 900, …) | rises with dose | composition shift; position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | 0.676× | -3.3 | 0.16 | 3/39 (HS-578T, PANC-1, …) | inconsistent across doses |  |
| [[Sinomenine (drug)]] 0.5 µM |  | 0.682× | -3.2 | 0.16 | 4/37 (LS 180, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.491× | -3.1 | 0.19 | 3/32 (RPMI-7951, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7747. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 7.43 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0685× (z -11.0) |
| [[A498 (line)]] | wt | 2.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.35× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 2.98 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.926 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.427 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.966 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.615 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.466 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.550 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.699 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.756 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.712 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.668 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.279 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7747), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KANK3]] | +0.60 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[CDH23]] | +0.57 | +0.37 / +0.67 | both halves | 8e-05 |  |
| [[HES2]] | +0.56 | +0.37 / +0.66 | both halves | 8e-05 |  |
| [[NFATC2IP-AS1]] | +0.56 | +0.35 / +0.58 | both halves | 1e-04 |  |
| [[MIR3659HG]] | +0.55 | +0.37 / +0.57 | both halves | 9e-05 |  |
| [[INSYN2A]] | +0.55 | +0.36 / +0.63 | both halves | 1e-04 |  |
| [[SLC26A5]] | +0.55 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[PLAC1]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[RFPL1S]] | +0.53 | +0.37 / +0.69 | both halves | 8e-05 |  |
| [[SCN1A-AS1]] | +0.53 | +0.32 / +0.60 | both halves | 1e-04 |  |
| [[ABCC11]] | +0.53 | +0.38 / +0.55 | both halves | 7e-05 |  |
| [[A2ML1-AS1]] | +0.52 | +0.32 / +0.61 | both halves | 2e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5PB]] | -0.60 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[C2CD5]] | -0.53 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[SLX4IP]] | -0.51 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[RAD51B]] | -0.50 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[SRP9]] | -0.49 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[FKTN]] | -0.48 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[GUF1]] | -0.47 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[ICE2]] | -0.47 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[ZNF678]] | -0.47 | -0.29 / -0.43 | both halves | 2e-04 |  |
| [[AGL]] | -0.46 | -0.29 / -0.41 | both halves | 2e-04 |  |
| [[MRPS10]] | -0.46 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[DCLRE1A]] | -0.46 | -0.30 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LGI4's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.8% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Ouabain (Octahydrate) (drug)]] 0.5 µM | C | LGI4 activity lowers the cells' numbers under Ouabain (Octahydrate) 0.5 µM (makes them more sensitive) | lines that do not express LGI4 (5) vs lines expressing it (43) | the lines without LGI4: 1.79× the cells of the other lines | 0.011 | ⚠ tissue-confounded; across organs; also absent: SLC25A43, FXYD5, NMI; maybe low, not absent |
| cells under [[Digitoxin (drug)]] 0.5 µM | C | LGI4 activity lowers the cells' numbers under Digitoxin 0.5 µM (makes them more sensitive) | lines that do not express LGI4 (5) vs lines expressing it (43) | the lines without LGI4: 1.55× the cells of the other lines | 0.026 | ⚠ tissue-confounded; across organs; also absent: SLC25A43, FXYD5, NMI; maybe low, not absent |
| cells under [[Vinblastine (sulfate) (drug)]] 0.05 µM | C | LGI4 activity lowers the cells' numbers under Vinblastine (sulfate) 0.05 µM (makes them more sensitive) | lines that do not express LGI4 (5) vs lines expressing it (43) | the lines without LGI4: 1.27× the cells of the other lines | 0.033 | ⚠ tissue-confounded; across organs; also absent: SLC25A43, FXYD5, NMI; maybe low, not absent |
| cells under [[Loperamide (hydrochloride) (drug)]] 0.5 µM | C | LGI4 activity lowers the cells' numbers under Loperamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express LGI4 (5) vs lines expressing it (43) | the lines without LGI4: 1.23× the cells of the other lines | 0.034 | ⚠ tissue-confounded; across organs; also absent: SLC25A43, FXYD5, NMI; maybe low, not absent |
| cells under [[Tucatinib (drug)]] 5 µM | C | LGI4 activity raises the cells' numbers under Tucatinib 5 µM (protects the cells) | lines that do not express LGI4 (5) vs lines expressing it (43) | the lines without LGI4: 0.74× the cells of the other lines | 0.038 | ⚠ tissue-confounded; across organs; also absent: SLC25A43, FXYD5, NMI; maybe low, not absent |
| cells under [[Betamethasone dipropionate (drug)]] 5 µM | C | LGI4 activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express LGI4 (5) vs lines expressing it (43) | the lines without LGI4: 0.75× the cells of the other lines | 0.039 | ⚠ tissue-confounded; across organs; also absent: SLC25A43, FXYD5, NMI; maybe low, not absent |
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | C | LGI4 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express LGI4 (5) vs lines expressing it (43) | the lines without LGI4: 0.78× the cells of the other lines | 0.055 | ⚠ tissue-confounded; across organs; also absent: SLC25A43, FXYD5, NMI; maybe low, not absent |
| cells under [[Rutin (trihydrate) (drug)]] 0.05 µM | C | LGI4 activity lowers the cells' numbers under Rutin (trihydrate) 0.05 µM (makes them more sensitive) | lines that do not express LGI4 (5) vs lines expressing it (43) | the lines without LGI4: 1.25× the cells of the other lines | 0.056 | ⚠ tissue-confounded; across organs; also absent: SLC25A43, FXYD5, NMI; maybe low, not absent |
| cells under [[Tranilast (drug)]] 0.5 µM | C | LGI4 activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express LGI4 (5) vs lines expressing it (43) | the lines without LGI4: 0.79× the cells of the other lines | 0.057 | ⚠ tissue-confounded; across organs; also absent: SLC25A43, FXYD5, NMI; maybe low, not absent |
| cells under [[Selinexor (drug)]] 5 µM | C | LGI4 activity lowers the cells' numbers under Selinexor 5 µM (makes them more sensitive) | lines that do not express LGI4 (5) vs lines expressing it (43) | the lines without LGI4: 1.41× the cells of the other lines | 0.088 | ⚠ tissue-confounded; across organs; also absent: SLC25A43, FXYD5, NMI; maybe low, not absent |
| cells under [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM | C | LGI4 activity raises the cells' numbers under Sivelestat (sodium tetrahydrate) 0.5 µM (protects the cells) | lines that do not express LGI4 (5) vs lines expressing it (43) | the lines without LGI4: 0.80× the cells of the other lines | 0.091 | ⚠ tissue-confounded; across organs; also absent: SLC25A43, FXYD5, NMI; maybe low, not absent |
| cells under [[Arbutin (drug)]] 5 µM | C | LGI4 activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express LGI4 (5) vs lines expressing it (43) | the lines without LGI4: 0.78× the cells of the other lines | 0.097 | ⚠ tissue-confounded; across organs; also absent: SLC25A43, FXYD5, NMI; maybe low, not absent |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.433). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.4, 34.0); signed map (26.0, 21.3). **Vector** length 41.5, 4.93% of its response variance represented; |z| ≥ 3 in 976 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +10.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +7.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +0.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.4 | +0.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -2.5 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.3 | -4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.8 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -3.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.3 | -3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -2.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat LGI family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:35,124,513-35,142,451 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | LGI family |
| Reactome | 1 pathways, smallest: LGI-ADAM interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N135](https://www.uniprot.org/uniprotkb/Q8N135) (Leucine-rich repeat LGI family member 4):

> Component of Schwann cell signaling pathway(s) that controls axon segregation and myelin formation (By similarity).

**Summary**, from NCBI Gene [163175](https://www.ncbi.nlm.nih.gov/gene/163175):

> Involved in regulation of myelination. Predicted to be located in extracellular region. Predicted to be active in obsolete extracellular space. Implicated in arthrogryposis multiplex congenita-1 and childhood absence epilepsy. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18712](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18712) · Entrez [163175](https://www.ncbi.nlm.nih.gov/gene/163175) · UniProt [Q8N135](https://www.uniprot.org/uniprotkb/Q8N135) · Ensembl [ENSG00000153902](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153902)

## Data

Gene col 7747: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7747); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7747, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7747]; `tensor/DDL_lfc|DDL_z.npy` [7747]; `embed/gene_vectors.npy` [7747]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7747 or target_col == 7747). Every well: [[LGI4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LGI4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
