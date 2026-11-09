---
symbol: "ESPN"
type: "gene"
col: 11877
ensembl_id: "ENSG00000187017"
name: "espin"
location: "1p36.31"
module: 100
arm: "+"
pooled_cpm: 5.81
n_lines_expressing: 24
n_dd_up: 24
n_dd_down: 5
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 10
direction_downstream: 16
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# ESPN

*espin* — 1p36.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 7.06× (z +18.4, q 0e+00, up in 21 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.607× (z -4.7, q 0.002, down in 13 of 21 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PADI2]] (+0.59, fdr 1e-04), [[AZGP1]] (+0.59, fdr 2e-05), [[NCMAP]] (+0.58, fdr 2e-05); moves opposite to [[ANXA2R-OT1]] (-0.47, fdr 1e-04), [[PRR14L]] (-0.47, fdr 2e-04), [[METTL4]] (-0.46, fdr 2e-04).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[CADM1]] → it (grade B ⚠); 16 go from it, the strongest it → [[EPHB3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11877.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **7.06×** | +18.4 | 0e+00 | 21/22 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.71×** | +16.4 | 0e+00 | 21/22 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.14×** | +15.3 | 0e+00 | 20/21 (SW1417, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **4.79×** | +14.8 | 0e+00 | 19/22 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.37×** | +13.4 | 1e-38 | 5/9 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.66×** | +13.0 | 8e-37 | 10/20 (PANC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +11.7 | 2e-29 | 10/19 (PANC-1, HCT15, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.80×** | +9.7 | 2e-20 | 8/12 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.62×** | +9.1 | 7e-18 | 18/22 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.32×** | +7.6 | 1e-12 | 8/20 (PANC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.62×** | +7.6 | 2e-12 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.92×** | +6.1 | 4e-08 | 12/21 (CFPAC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +5.5 | 1e-06 | 3/12 (CFPAC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.54×** | +4.6 | 2e-04 | 11/21 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +4.5 | 3e-04 | 2/10 (BT-474, HepG2/C3A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.94×** | +4.5 | 3e-04 | 2/14 (SW480, NCI-H2347) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.007 | 2/15 (HepG2/C3A, SK-MEL-2) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.70×** | +3.6 | 0.011 | 2/12 (HepG2/C3A, HOP62) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.064 | 4/21 (BT-474, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.37×** | +3.0 | 0.074 | 4/21 (HOP62, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11877.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.607×** | -4.7 | 0.002 | 13/21 (HepG2/C3A, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Fusidic acid (drug)]] 5 µM |  | **0.739×** | -4.0 | 0.017 | 6/22 (NCI-H661, NCI-H2347, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.686×** | -3.5 | 0.064 | 8/22 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.689×** | -3.5 | 0.064 | 10/21 (HepG2/C3A, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.697×** | -3.4 | 0.076 | 9/21 (AsPC-1, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11877. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 82.3 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.205× (z -10.9) |
| [[PANC-1 (line)]] | alt | 6.84 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 17.4× (z +13.7) | — |
| [[CFPAC-1 (line)]] | alt | 7.28 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 13.5× (z +12.6) | — |
| [[HOP62 (line)]] | alt | 3.57 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 13.0× (z +9.6) | [[Sunitinib (drug)]] 5 µM 0.0797× (z -9.4) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 2.48 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 30.8× (z +8.8) | [[Quinestrol (drug)]] 5 µM 0.0929× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.103× (z -10.2) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.242× (z -9.4) |
| [[SW1417 (line)]] | alt | 7.10 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.92× (z +9.1) | — |
| [[LoVo (line)]] | wt | 21.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.23× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 20.6 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.10× (z +10.4) | — |
| [[SW480 (line)]] | alt | 18.7 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.237× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 5.26 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 11.9× (z +8.6) | — |
| [[A-172 (line)]] | wt | 0.756 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.706 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.971 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.705 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.670 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.690 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.781 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.822 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.806 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.578 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.664 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.641 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.798 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.31 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11877), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 11 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PADI2]] | +0.59 | +0.35 / +0.61 | both halves | 1e-04 |  |
| [[AZGP1]] | +0.59 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[NCMAP]] | +0.58 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[FOXO6]] | +0.53 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[CADM1]] | +0.52 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[RNF24]] | +0.52 | +0.29 / +0.56 | both halves | 2e-04 |  |
| [[FGFR4]] | +0.51 | +0.39 / +0.46 | both halves | 6e-05 |  |
| [[EPHB3]] | +0.51 | +0.35 / +0.52 | both halves | 1e-04 |  |
| [[SLC7A8]] | +0.50 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[SMARCD3]] | +0.50 | +0.30 / +0.48 | both halves | 2e-04 |  |
| [[VIL1]] | +0.50 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[F10]] | +0.50 | +0.47 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANXA2R-OT1]] | -0.47 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[PRR14L]] | -0.47 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[METTL4]] | -0.46 | -0.29 / -0.46 | both halves | 2e-04 |  |
| [[IREB2]] | -0.44 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[SPRY3]] | -0.44 | -0.14 / -0.55 | ⚠ one half (not replicated) | 0.002 |  |
| [[GPATCH2]] | -0.44 | -0.18 / -0.36 | ⚠ not reproduced | 1e-03 |  |
| [[DPH5-DT]] | -0.43 | -0.16 / -0.38 | ⚠ not reproduced | 0.001 |  |
| [[HECTD1]] | -0.43 | -0.26 / -0.44 | both halves | 4e-04 | same gene group |
| [[MCPH1]] | -0.43 | -0.18 / -0.41 | ⚠ not reproduced | 1e-03 |  |
| [[RNPC3-DT]] | -0.43 | -0.24 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[AVEN]] | -0.42 | -0.22 / -0.46 | both halves | 6e-04 |  |
| [[ANKMY1]] | -0.42 | -0.22 / -0.37 | both halves | 6e-04 | same gene group |
| [[HMGA1P4]] | -0.42 | -0.21 / -0.40 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 3, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CADM1]] | B | CADM1 activity raises ESPN's level | lines that do not express CADM1 (18) vs lines expressing it (32) | 2.00× lower at baseline in the lines without CADM1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, BEND6, ARNT2 |
| [[CRACR2B]] | B | CRACR2B activity raises ESPN's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 2.39× lower at baseline in the lines without CRACR2B | 0.046 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[EPHB3]] | B | EPHB3 activity raises ESPN's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 1.46× lower at baseline in the lines without EPHB3 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| [[TJP3]] | C | TJP3 activity raises ESPN's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.84× lower at baseline in the lines without TJP3 | 0.006 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1; co-absent with the target |
| [[ATP2C2]] | C | ATP2C2 activity raises ESPN's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 2.09× lower at baseline in the lines without ATP2C2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14; co-absent with the target |
| [[TMEM139]] | C | TMEM139 activity raises ESPN's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 2.41× lower at baseline in the lines without TMEM139 | 0.035 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A; co-absent with the target |
| [[LRG1]] | C | LRG1 activity raises ESPN's level | lines that do not express LRG1 (28) vs lines expressing it (22) | 2.47× lower at baseline in the lines without LRG1 | 0.036 | ⚠ within organs, on part of the lines; also absent: RORC, LAD1, EPCAM; co-absent with the target |
| [[ENPP5]] | C | ENPP5 activity raises ESPN's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 1.93× lower at baseline in the lines without ENPP5 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004; co-absent with the target |
| [[NCMAP]] | C | NCMAP activity raises ESPN's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 2.25× lower at baseline in the lines without NCMAP | 0.061 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent; co-absent with the target |
| [[RAB17]] | C | RAB17 activity raises ESPN's level | lines that do not express RAB17 (22) vs lines expressing it (28) | 2.32× lower at baseline in the lines without RAB17 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MAL2, TNNT2, BSPRY; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 9, C 7. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHB3]] | B | ESPN activity raises EPHB3's level | lines that do not express ESPN (26) vs lines expressing it (24) | 2.32× lower at baseline in the lines without ESPN | 0.020 | ⚠ within organs, on part of the lines; also absent: B3GNT7, HSD17B2, FXYD3 |
| [[BIK]] | B | ESPN activity raises BIK's level | lines that do not express ESPN (26) vs lines expressing it (24) | 2.24× lower at baseline in the lines without ESPN | 0.053 | ⚠ within organs, on part of the lines; also absent: B3GNT7, HSD17B2, FXYD3 |
| [[AFDN]] | B | ESPN activity raises AFDN's level | lines that do not express ESPN (26) vs lines expressing it (24) | 1.57× lower at baseline in the lines without ESPN | 0.057 | ⚠ within organs, on part of the lines; also absent: B3GNT7, HSD17B2, FXYD3 |
| [[FGFR4]] | B | ESPN activity raises FGFR4's level | lines that do not express ESPN (26) vs lines expressing it (24) | 1.55× lower at baseline in the lines without ESPN | 0.060 | ⚠ within organs, on part of the lines; also absent: B3GNT7, HSD17B2, FXYD3 |
| [[CDK18]] | B | ESPN activity raises CDK18's level | lines that do not express ESPN (26) vs lines expressing it (24) | 1.51× lower at baseline in the lines without ESPN | 0.068 | ⚠ within organs, on part of the lines; also absent: B3GNT7, HSD17B2, FXYD3 |
| [[CRACR2B]] | B | ESPN activity raises CRACR2B's level | lines that do not express ESPN (26) vs lines expressing it (24) | 1.86× lower at baseline in the lines without ESPN | 0.068 | ⚠ within organs, on part of the lines; also absent: B3GNT7, HSD17B2, FXYD3 |
| [[NOS1AP]] | B | ESPN activity raises NOS1AP's level | lines that do not express ESPN (26) vs lines expressing it (24) | 1.83× lower at baseline in the lines without ESPN | 0.080 | ⚠ within organs, on part of the lines; also absent: B3GNT7, HSD17B2, FXYD3 |
| [[F10]] | B | ESPN activity raises F10's level | lines that do not express ESPN (26) vs lines expressing it (24) | 1.53× lower at baseline in the lines without ESPN | 0.094 | ⚠ within organs, on part of the lines; also absent: B3GNT7, HSD17B2, FXYD3 |
| [[SLC7A8]] | B | ESPN activity raises SLC7A8's level | lines that do not express ESPN (26) vs lines expressing it (24) | 1.93× lower at baseline in the lines without ESPN | 0.094 | ⚠ within organs, on part of the lines; also absent: B3GNT7, HSD17B2, FXYD3 |
| [[TJP3]] | C | ESPN activity raises TJP3's level | lines that do not express ESPN (26) vs lines expressing it (24) | 2.68× lower at baseline in the lines without ESPN | 0.029 | ⚠ within organs, on part of the lines; also absent: B3GNT7, HSD17B2, FXYD3; co-absent with the target |
| [[RAB17]] | C | ESPN activity raises RAB17's level | lines that do not express ESPN (26) vs lines expressing it (24) | 3.21× lower at baseline in the lines without ESPN | 0.044 | ⚠ within organs, on part of the lines; also absent: B3GNT7, HSD17B2, FXYD3; co-absent with the target |
| [[COL9A3]] | C | ESPN activity raises COL9A3's level | lines that do not express ESPN (26) vs lines expressing it (24) | 2.99× lower at baseline in the lines without ESPN | 0.057 | ⚠ within organs, on part of the lines; also absent: B3GNT7, HSD17B2, FXYD3; co-absent with the target |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.447). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.1, 51.0); signed map (68.9, 15.8). **Vector** length 53.2, 12.6% of its response variance represented; |z| ≥ 3 in 570 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +15.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.8 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +3.8 | +9.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +13.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.4 | +7.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.1 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.1 | -0.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -4.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -3.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -2.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -0.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | espin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.31 — chr1:6,424,776-6,461,367 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DFNB36 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Reactome | 4 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound by inner hair cells of the cochlea; Sensory processing of sound |
| Matched by | ensembl_id |

**Function**, from UniProt [B1AK53](https://www.uniprot.org/uniprotkb/B1AK53) (Espin):

> Multifunctional actin-bundling protein. Plays a major role in regulating the organization, dimension, dynamics and signaling capacities of the actin filament-rich microvilli in the mechanosensory and chemosensory cells. Required for the assembly and stabilization of the stereociliary parallel actin bundles. Plays a crucial role in the formation and maintenance of inner ear hair cell stereocilia (By similarity). Involved in the elongation of actin in stereocilia. In extrastriolar hair cells, …

**Summary**, from NCBI Gene [83715](https://www.ncbi.nlm.nih.gov/gene/83715):

> This gene encodes a multifunctional actin-bundling protein. It plays a major role in regulating the organization, dimensions, dynamics, and signaling capacities of the actin filament-rich, microvillus-type specializations that mediate sensory transduction in various mechanosensory and chemosensory cells. Mutations in this gene are associated with autosomal recessive neurosensory deafness, and autosomal dominant sensorineural deafness without vestibular involvement. [provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:13281](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13281) · Entrez [83715](https://www.ncbi.nlm.nih.gov/gene/83715) · UniProt [B1AK53](https://www.uniprot.org/uniprotkb/B1AK53) · Ensembl [ENSG00000187017](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187017)

## Data

Gene col 11877: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11877); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11877, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11877]; `tensor/DDL_lfc|DDL_z.npy` [11877]; `embed/gene_vectors.npy` [11877]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11877 or target_col == 11877). Every well: [[ESPN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ESPN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
