---
symbol: "C4orf33"
type: "gene"
col: 7525
ensembl_id: "ENSG00000151470"
name: "chromosome 4 open reading frame 33"
location: "4q28.2"
module: 32
arm: "+"
pooled_cpm: 7.33
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 20
n_dd_up_clean: 21
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 14
direction_downstream: 2
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# C4orf33

*chromosome 4 open reading frame 33* — 4q28.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.31× (z +14.0, q 1e-41, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.454× (z -8.7, q 3e-15, down in 29 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM34]] (+0.67, fdr 7e-06), [[HERC5]] (+0.66, fdr 7e-06), [[STAT1]] (+0.65, fdr 7e-06); moves opposite to [[RILPL1]] (-0.56, fdr 1e-05), [[NBPF15]] (-0.55, fdr 1e-05), [[PPP1R26-AS1]] (-0.53, fdr 3e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[RSAD2]] → it (grade B ⚠); 2 go from it, the strongest it → [[PARP10]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7525.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.31×** | +14.0 | 1e-41 | 45/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.19×** | +13.5 | 3e-39 | 46/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.34×** | +12.7 | 6e-35 | 41/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.24×** | +9.1 | 2e-17 | 4/11 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.64×** | +8.2 | 2e-14 | 20/41 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.08×** | +7.9 | 3e-13 | 17/22 (A-172, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.93×** | +7.7 | 1e-12 | 19/30 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.84×** | +7.1 | 9e-11 | 26/47 (SW1417, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.47×** | +6.4 | 1e-08 | 21/41 (SW1417, PANC-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.66×** | +5.7 | 6e-07 | 23/45 (PANC-1, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +5.4 | 4e-06 | 17/44 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~12% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **1.43×** | +4.5 | 4e-04 | 14/48 (LoVo, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +4.4 | 5e-04 | 12/46 (LS 180, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.44×** | +4.3 | 8e-04 | 16/46 (LoVo, C32, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.001 | 13/48 (SW1417, A498, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +3.9 | 0.004 | 12/41 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.27×** | +3.8 | 0.004 | 16/47 (RPMI-7951, SK-MEL-2, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.87×** | +3.8 | 0.004 | 6/46 (HEC-1-A, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.009 | 3/48 (NCI-H2030, A498, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7525.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.454×** | -8.7 | 3e-15 | 29/43 (SK-MEL-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.509×** | -7.8 | 1e-12 | 27/47 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.644×** | -7.2 | 1e-10 | 31/47 (NCI-H1573, SHP-77, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.574×** | -5.8 | 7e-07 | 23/46 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.611×** | -5.7 | 1e-06 | 21/41 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.626×** | -5.4 | 5e-06 | 16/47 (KATO III, SW480, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.649×** | -5.0 | 4e-05 | 19/47 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.642×** | -4.9 | 6e-05 | 18/46 (BT-474, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.645×** | -4.6 | 3e-04 | 20/46 (KATO III, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.680×** | -4.5 | 5e-04 | 17/47 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.701×** | -4.1 | 0.002 | 18/47 (BT-474, NCI-H23, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.732×** | -3.6 | 0.014 | 13/45 (NCI-H1573, NCI-H2030, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.710×** | -3.6 | 0.015 | 14/46 (PANC-1, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.739×** | -3.5 | 0.019 | 12/45 (SNU-423, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.756×** | -3.2 | 0.047 | 18/41 (C32, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.766×** | -3.1 | 0.074 | 8/46 (NCI-H1792, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.694×** | -3.0 | 0.081 | 11/47 (A498, NCI-H661, …) | all doses, flat | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.615×** | -2.9 | 0.093 | 10/37 (Hs 766T, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.776×** | -2.9 | 0.093 | 14/46 (NCI-H23, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7525. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 16.6 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.205× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.298× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 5.73 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -9.1) |
| [[HT-29 (line)]] | alt | 8.91 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.109× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 7.79 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0887× (z -8.9) |
| [[SNU-423 (line)]] | alt | 7.09 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0844× (z -10.1) |
| [[A-172 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.98 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.12 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7525), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM34]] | +0.67 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[HERC5]] | +0.66 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[STAT1]] | +0.65 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[IFIT1]] | +0.65 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[TRANK1]] | +0.64 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[SAMHD1]] | +0.64 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[OAS2]] | +0.62 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[IFI44]] | +0.62 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[GCA]] | +0.61 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[OASL]] | +0.61 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[IFIT2]] | +0.60 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[OAS3]] | +0.60 | +0.60 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RILPL1]] | -0.56 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[NBPF15]] | -0.55 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[PPP1R26-AS1]] | -0.53 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[NLN]] | -0.52 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[CMTM4]] | -0.51 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[CAPN15]] | -0.51 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[PTPN9]] | -0.51 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[MPP3]] | -0.50 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[C9orf153]] | -0.50 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[RABEPK]] | -0.50 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[KLC1]] | -0.50 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[RUSC2]] | -0.50 | -0.53 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 12, C 2. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RSAD2]] | B | RSAD2 activity raises C4orf33's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 1.51× lower at baseline in the lines without RSAD2 | 0.013 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[ETV7]] | B | ETV7 activity raises C4orf33's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 1.50× lower at baseline in the lines without ETV7 | 0.015 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |
| [[GBP4]] | B | GBP4 activity raises C4orf33's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.32× lower at baseline in the lines without GBP4 | 0.019 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[SAMD9L]] | B | SAMD9L activity raises C4orf33's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 1.42× lower at baseline in the lines without SAMD9L | 0.021 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[TLR3]] | B | TLR3 activity raises C4orf33's level | lines that do not express TLR3 (12) vs lines expressing it (38) | 1.53× lower at baseline in the lines without TLR3 | 0.031 | ⚠ within organs, on part of the lines; also absent: LGALS3, GBP4, RAB27B; maybe low, not absent |
| [[MX1]] | B | MX1 activity raises C4orf33's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.31× lower at baseline in the lines without MX1 | 0.055 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[IFIT2]] | B | IFIT2 activity raises C4orf33's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 1.43× lower at baseline in the lines without IFIT2 | 0.068 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[UBA7]] | B | UBA7 activity raises C4orf33's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 1.45× lower at baseline in the lines without UBA7 | 0.068 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[IFI16]] | B | IFI16 activity raises C4orf33's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 1.23× lower at baseline in the lines without IFI16 | 0.078 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[MAP2K1]] | B | MAP2K1 activity lowers C4orf33's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[IFI44]] | B | IFI44 activity raises C4orf33's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 1.34× lower at baseline in the lines without IFI44 | 0.086 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[TRANK1]] | B | TRANK1 activity raises C4orf33's level | lines that do not express TRANK1 (7) vs lines expressing it (43) | 1.36× lower at baseline in the lines without TRANK1 | 0.0999 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARP10]] | C | C4orf33's natural level strengthens PARP10's drug response | C4orf33's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.68, reverse -0.34; direction not clear | 0.034 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PSMB8]] | C | C4orf33's natural level strengthens PSMB8's drug response | C4orf33's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.65, reverse -0.27; direction not clear | 0.083 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.598). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.9, 53.9); signed map (66.2, 31.8). **Vector** length 79.8, 15.2% of its response variance represented; |z| ≥ 3 in 1,131 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.51 to 56); *interferon gamma response* (hallmark, mean cos +0.50 to 60); *interferon* (control, mean cos +0.58 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +4.8 | +7.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +4.5 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +4.0 | +7.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.3 | +5.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +0.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +5.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.2 | +4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +2.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.1 | +3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.0 | +2.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -4.7 | -8.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.5 | -7.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.7 | -7.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -5.0 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.1 | -4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.0 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.7 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 4 open reading frame 33 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q28.2 — chr4:129,093,317-129,116,640 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33703 |
| Matched by | ensembl_id |

UniProt [Q8N1A6](https://www.uniprot.org/uniprotkb/Q8N1A6) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27025](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27025) · Entrez [132321](https://www.ncbi.nlm.nih.gov/gene/132321) · UniProt [Q8N1A6](https://www.uniprot.org/uniprotkb/Q8N1A6) · Ensembl [ENSG00000151470](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151470)

## Data

Gene col 7525: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7525); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7525, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7525]; `tensor/DDL_lfc|DDL_z.npy` [7525]; `embed/gene_vectors.npy` [7525]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7525 or target_col == 7525). Every well: [[C4orf33 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C4orf33.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
